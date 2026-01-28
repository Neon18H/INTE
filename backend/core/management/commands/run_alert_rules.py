from django.core.management.base import BaseCommand
from core.models import AlertEvent, AlertRule, Indicator, IndicatorObservation


class Command(BaseCommand):
    help = "Evaluate alert rules against indicators"

    def handle(self, *args, **options):
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
        self.stdout.write(self.style.SUCCESS(f"Created {created} alerts."))
