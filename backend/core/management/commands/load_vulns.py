import json
from pathlib import Path
from django.core.management.base import BaseCommand
from core.models import Vulnerability


class Command(BaseCommand):
    help = "Load vulnerability dataset from JSON file"

    def add_arguments(self, parser):
        parser.add_argument("--path", default="backend/data/demo_vulns.json")

    def handle(self, *args, **options):
        path = Path(options["path"])
        payload = json.loads(path.read_text())
        created = 0
        for item in payload:
            vuln, is_created = Vulnerability.objects.get_or_create(
                cve=item["cve"],
                defaults={
                    "title": item["title"],
                    "description": item["description"],
                    "cvss": item["cvss"],
                    "epss": item["epss"],
                    "kev_flag": item["kev_flag"],
                    "published_date": item["published_date"],
                    "vendor": item["vendor"],
                    "product": item["product"],
                    "references_json": item["references_json"],
                },
            )
            if is_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Loaded {created} vulnerabilities."))
