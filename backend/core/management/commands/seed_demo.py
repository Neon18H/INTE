from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import (
    AlertRule,
    Campaign,
    Indicator,
    IndicatorObservation,
    MalwareFamily,
    Role,
    ThreatActor,
)
from django.utils import timezone


class Command(BaseCommand):
    help = "Seed demo data for CTI platform"

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="analyst").exists():
            user = User.objects.create_user(username="analyst", password="analyst123", is_staff=True)
            role, _ = Role.objects.get_or_create(name="analyst")
            role.users.add(user)

        actor = ThreatActor.objects.create(name="Shadow Lynx", description="Regional APT")
        malware = MalwareFamily.objects.create(name="BlackFang", description="Ransomware family")
        campaign = Campaign.objects.create(name="Operation Dusk", summary="Targeted phishing")
        campaign.actors.add(actor)
        campaign.malware_families.add(malware)

        indicator = Indicator.objects.create(type="domain", value="malicious.example", normalized="malicious.example")
        indicator.campaigns.add(campaign)
        indicator.malware_families.add(malware)

        IndicatorObservation.objects.create(
            indicator=indicator,
            source="seed",
            first_seen=timezone.now(),
            last_seen=timezone.now(),
            confidence=80,
            severity=4,
            tags=["phishing", "demo"],
            note="Seeded observation",
        )

        AlertRule.objects.get_or_create(name="High Severity", match_type="severity_threshold", value="4")
        self.stdout.write(self.style.SUCCESS("Demo data seeded."))
