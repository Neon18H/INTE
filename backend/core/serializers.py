from rest_framework import serializers
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


class IndicatorObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorObservation
        fields = "__all__"


class IndicatorSerializer(serializers.ModelSerializer):
    observations = IndicatorObservationSerializer(many=True, read_only=True)

    class Meta:
        model = Indicator
        fields = "__all__"

    def validate(self, attrs):
        attrs["normalized"] = attrs.get("value", "").strip().lower()
        return attrs


class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = "__all__"


class ThreatActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatActor
        fields = "__all__"


class MalwareFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = MalwareFamily
        fields = "__all__"


class CampaignSerializer(serializers.ModelSerializer):
    actors = ThreatActorSerializer(many=True, read_only=True)
    malware_families = MalwareFamilySerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = "__all__"


class AlertRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertRule
        fields = "__all__"


class AlertEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertEvent
        fields = "__all__"


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"
