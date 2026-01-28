from django.contrib import admin
from .models import (
    AlertEvent,
    AlertRule,
    AuditLog,
    Campaign,
    Indicator,
    IndicatorObservation,
    MalwareFamily,
    Role,
    ThreatActor,
    Vulnerability,
)

admin.site.register(Indicator)
admin.site.register(IndicatorObservation)
admin.site.register(Vulnerability)
admin.site.register(ThreatActor)
admin.site.register(MalwareFamily)
admin.site.register(Campaign)
admin.site.register(AlertRule)
admin.site.register(AlertEvent)
admin.site.register(Role)
admin.site.register(AuditLog)
