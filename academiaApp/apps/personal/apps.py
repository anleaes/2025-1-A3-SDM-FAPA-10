from django import forms

from apps.personal.models import Personal


class PersonalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.personal"
    verbose_name = "Personal"
