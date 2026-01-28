from django.conf import settings
from django.db import models


class Indicator(models.Model):
    INDICATOR_TYPES = [
        ("ip", "IP"),
        ("domain", "Domain"),
        ("url", "URL"),
        ("hash", "Hash"),
        ("email", "Email"),
        ("cert", "Certificate"),
    ]

    type = models.CharField(max_length=20, choices=INDICATOR_TYPES)
    value = models.CharField(max_length=255)
    normalized = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    campaigns = models.ManyToManyField("Campaign", blank=True, related_name="indicators")
    malware_families = models.ManyToManyField("MalwareFamily", blank=True, related_name="indicators")

    def __str__(self) -> str:
        return f"{self.type}:{self.value}"


class IndicatorObservation(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, related_name="observations")
    source = models.CharField(max_length=120)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()
    confidence = models.PositiveIntegerField(default=50)
    severity = models.PositiveIntegerField(default=3)
    tags = models.JSONField(default=list)
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.indicator} @ {self.source}"


class Vulnerability(models.Model):
    cve = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    cvss = models.FloatField()
    epss = models.FloatField()
    kev_flag = models.BooleanField(default=False)
    published_date = models.DateField()
    vendor = models.CharField(max_length=120)
    product = models.CharField(max_length=120)
    references_json = models.JSONField(default=list)

    def __str__(self) -> str:
        return self.cve


class ThreatActor(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=80, blank=True)

    def __str__(self) -> str:
        return self.name


class MalwareFamily(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    first_seen = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=120)
    summary = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(ThreatActor, blank=True, related_name="campaigns")
    malware_families = models.ManyToManyField(MalwareFamily, blank=True, related_name="campaigns")

    def __str__(self) -> str:
        return self.name


class AlertRule(models.Model):
    MATCH_TYPES = [
        ("keyword", "Keyword"),
        ("tag", "Tag"),
        ("ioc_type", "IOC Type"),
        ("severity_threshold", "Severity Threshold"),
    ]

    name = models.CharField(max_length=120)
    match_type = models.CharField(max_length=40, choices=MATCH_TYPES)
    value = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class AlertEvent(models.Model):
    rule = models.ForeignKey(AlertRule, on_delete=models.CASCADE, related_name="events")
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True, blank=True)
    severity = models.PositiveIntegerField(default=3)
    status = models.CharField(max_length=20, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    detail = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.rule.name} - {self.status}"


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="roles")

    def __str__(self) -> str:
        return self.name


class AuditLog(models.Model):
    ACTIONS = [
        ("create", "Create"),
        ("update", "Update"),
        ("delete", "Delete"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=10, choices=ACTIONS)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    changes = models.JSONField(default=dict)

    def __str__(self) -> str:
        return f"{self.model_name} {self.action}"
