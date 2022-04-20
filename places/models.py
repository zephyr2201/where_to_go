from django.db import models
from django.utils.translation import gettext_lazy as _

from places.utils import file_path


class Location(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description_short = models.TextField(
        null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title


class LocationPhoto(models.Model):
    file = models.ImageField(
        _('Файл'),
        upload_to=file_path,
        null=True,
    )
    location =  models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='images'
    )


class Coordinates(models.Model):
    langitude = models.CharField(
        max_length=255,
        null=True, blank=True
        )
    lotitude = models.CharField(
        max_length=255,
        null=True, blank=True
    )
    location = models.OneToOneField(
        Location,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
