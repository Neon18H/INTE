from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core import views

router = routers.DefaultRouter()
router.register(r"indicators", views.IndicatorViewSet)
router.register(r"observations", views.IndicatorObservationViewSet)
router.register(r"vulnerabilities", views.VulnerabilityViewSet)
router.register(r"threat-actors", views.ThreatActorViewSet)
router.register(r"malware-families", views.MalwareFamilyViewSet)
router.register(r"campaigns", views.CampaignViewSet)
router.register(r"alert-rules", views.AlertRuleViewSet)
router.register(r"alert-events", views.AlertEventViewSet)
router.register(r"audit-logs", views.AuditLogViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/", include(router.urls)),
    path("api/v1/alerts/run/", views.run_alert_rules, name="run_alert_rules"),
    path("api/v1/dashboard/", views.dashboard_metrics, name="dashboard_metrics"),
]
