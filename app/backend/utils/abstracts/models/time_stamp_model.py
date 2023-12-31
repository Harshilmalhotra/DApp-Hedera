# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.utils import timezone

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.fields import  CreationDateTimeField, ModificationDateTimeField


class TimeStampedModel(models.Model):
    """
    TimeStampedModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """

    creation_date = CreationDateTimeField(_('creation date'))
    update_date = models.DateTimeField(_('update_date'), blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.update_date = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        get_latest_by = 'update_date'
        abstract = True