from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import LeaveBalance # This is now safe

@receiver(post_save, sender=User)
def create_user_leave_balance(sender, instance, created, **kwargs):
    if created:
        LeaveBalance.objects.create(staff_id=instance, year=2026)