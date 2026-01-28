from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import AuditLog


@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    if sender.__name__ in {"AuditLog"}:
        return
    if not hasattr(instance, "id"):
        return
    AuditLog.objects.create(
        user=getattr(instance, "_actor", None),
        action="create" if created else "update",
        model_name=sender.__name__,
        object_id=str(instance.pk),
        changes={},
    )


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender.__name__ in {"AuditLog"}:
        return
    AuditLog.objects.create(
        user=getattr(instance, "_actor", None),
        action="delete",
        model_name=sender.__name__,
        object_id=str(instance.pk),
        changes={},
    )
