from datetime import date
from django.db.models import Count
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .enrichment import trigger_enrichment
from .models import (
    AlertEvent,
    AlertRule,
    AuditLog,
    Campaign,
    Indicator,
    IndicatorObservation,
    MalwareFamily,
    ThreatActor,
    Vulnerability,
)
from .permissions import IsAdminOrAnalyst
from .serializers import (
    AlertEventSerializer,
    AlertRuleSerializer,
    AuditLogSerializer,
    CampaignSerializer,
    IndicatorObservationSerializer,
    IndicatorSerializer,
    MalwareFamilySerializer,
    ThreatActorSerializer,
    VulnerabilitySerializer,
)


class BaseAuditViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrAnalyst]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance._actor = self.request.user
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance._actor = self.request.user
        instance.save()

    def perform_destroy(self, instance):
        instance._actor = self.request.user
        instance.delete()


class IndicatorViewSet(BaseAuditViewSet):
    queryset = Indicator.objects.all().order_by("-created_at")
    serializer_class = IndicatorSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance._actor = self.request.user
        instance.save()
        trigger_enrichment(instance.id)


class IndicatorObservationViewSet(BaseAuditViewSet):
    queryset = IndicatorObservation.objects.all().order_by("-last_seen")
    serializer_class = IndicatorObservationSerializer


class VulnerabilityViewSet(BaseAuditViewSet):
    queryset = Vulnerability.objects.all().order_by("-published_date")
    serializer_class = VulnerabilitySerializer


class ThreatActorViewSet(BaseAuditViewSet):
    queryset = ThreatActor.objects.all().order_by("name")
    serializer_class = ThreatActorSerializer


class MalwareFamilyViewSet(BaseAuditViewSet):
    queryset = MalwareFamily.objects.all().order_by("name")
    serializer_class = MalwareFamilySerializer


class CampaignViewSet(BaseAuditViewSet):
    queryset = Campaign.objects.all().order_by("name")
    serializer_class = CampaignSerializer


class AlertRuleViewSet(BaseAuditViewSet):
    queryset = AlertRule.objects.all().order_by("name")
    serializer_class = AlertRuleSerializer


class AlertEventViewSet(BaseAuditViewSet):
    queryset = AlertEvent.objects.all().order_by("-created_at")
    serializer_class = AlertEventSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = AuditLog.objects.all().order_by("-timestamp")
    serializer_class = AuditLogSerializer


@api_view(["POST"])
@permission_classes([IsAdminUser])
def run_alert_rules(request):
    created = 0
    rules = AlertRule.objects.filter(is_active=True)
    indicators = Indicator.objects.all()
    for rule in rules:
        for indicator in indicators:
            matched = False
            if rule.match_type == "keyword" and rule.value.lower() in indicator.value.lower():
                matched = True
            if rule.match_type == "ioc_type" and rule.value == indicator.type:
                matched = True
            if rule.match_type == "tag":
                if IndicatorObservation.objects.filter(indicator=indicator, tags__contains=[rule.value]).exists():
                    matched = True
            if rule.match_type == "severity_threshold":
                if IndicatorObservation.objects.filter(indicator=indicator, severity__gte=int(rule.value)).exists():
                    matched = True
            if matched:
                AlertEvent.objects.create(
                    rule=rule,
                    indicator=indicator,
                    severity=4,
                    detail=f"Matched rule {rule.name} for {indicator.value}",
                )
                created += 1
    return Response({"created": created})


@api_view(["GET"])
@permission_classes([IsAdminOrAnalyst])
def dashboard_metrics(request):
    today = date.today()
    iocs_today = Indicator.objects.filter(created_at__date=today).count()
    kev_count = Vulnerability.objects.filter(kev_flag=True).count()
    open_alerts = AlertEvent.objects.filter(status="open").count()
    top_severities = (
        IndicatorObservation.objects.values("severity")
        .annotate(total=Count("id"))
        .order_by("-total")
    )
    return Response(
        {
            "iocs_today": iocs_today,
            "kev_count": kev_count,
            "open_alerts": open_alerts,
            "top_severities": list(top_severities),
            "time": timezone.now().isoformat(),
        }
    )
