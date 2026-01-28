# Generated manually for initial schema
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AlertRule",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("match_type", models.CharField(choices=[("keyword", "Keyword"), ("tag", "Tag"), ("ioc_type", "IOC Type"), ("severity_threshold", "Severity Threshold")], max_length=40)),
                ("value", models.CharField(max_length=120)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="AuditLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(choices=[("create", "Create"), ("update", "Update"), ("delete", "Delete")], max_length=10)),
                ("model_name", models.CharField(max_length=100)),
                ("object_id", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("changes", models.JSONField(default=dict)),
                ("user", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Campaign",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("summary", models.TextField(blank=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Indicator",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("type", models.CharField(choices=[("ip", "IP"), ("domain", "Domain"), ("url", "URL"), ("hash", "Hash"), ("email", "Email"), ("cert", "Certificate")], max_length=20)),
                ("value", models.CharField(max_length=255)),
                ("normalized", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="MalwareFamily",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("first_seen", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True)),
                ("users", models.ManyToManyField(related_name="roles", to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="ThreatActor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("region", models.CharField(blank=True, max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="Vulnerability",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cve", models.CharField(max_length=30, unique=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("cvss", models.FloatField()),
                ("epss", models.FloatField()),
                ("kev_flag", models.BooleanField(default=False)),
                ("published_date", models.DateField()),
                ("vendor", models.CharField(max_length=120)),
                ("product", models.CharField(max_length=120)),
                ("references_json", models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name="IndicatorObservation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("source", models.CharField(max_length=120)),
                ("first_seen", models.DateTimeField()),
                ("last_seen", models.DateTimeField()),
                ("confidence", models.PositiveIntegerField(default=50)),
                ("severity", models.PositiveIntegerField(default=3)),
                ("tags", models.JSONField(default=list)),
                ("note", models.TextField(blank=True)),
                ("indicator", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="observations", to="core.indicator")),
            ],
        ),
        migrations.CreateModel(
            name="AlertEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("severity", models.PositiveIntegerField(default=3)),
                ("status", models.CharField(default="open", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("detail", models.TextField(blank=True)),
                ("indicator", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="core.indicator")),
                ("rule", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="events", to="core.alertrule")),
            ],
        ),
        migrations.AddField(
            model_name="campaign",
            name="actors",
            field=models.ManyToManyField(blank=True, related_name="campaigns", to="core.threatactor"),
        ),
        migrations.AddField(
            model_name="campaign",
            name="malware_families",
            field=models.ManyToManyField(blank=True, related_name="campaigns", to="core.malwarefamily"),
        ),
        migrations.AddField(
            model_name="indicator",
            name="campaigns",
            field=models.ManyToManyField(blank=True, related_name="indicators", to="core.campaign"),
        ),
        migrations.AddField(
            model_name="indicator",
            name="malware_families",
            field=models.ManyToManyField(blank=True, related_name="indicators", to="core.malwarefamily"),
        ),
    ]
