from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStamp):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserLocation(models.Model):
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = True
