from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from tinymce.models import HTMLField

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
    description_long = HTMLField(
        null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title
 
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локаций"


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

    @property
    def image_tag(self):
        if self.file:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.file.url))
        return ""

    def __str__(self) -> str:
        return 'Фото-' + self.location.title

    class Meta:
        verbose_name = "Фото локаций"
        verbose_name_plural = "Фото локаций"


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
        null=True, blank=True,
        related_name='coordinates'
    )

    class Meta:
        verbose_name = "Координаты локаций"
        verbose_name_plural = "Координаты локаций"
