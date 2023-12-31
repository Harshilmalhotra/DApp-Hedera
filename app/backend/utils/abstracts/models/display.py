# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models


class DisplayModel(models.Model):
    """
    DisplayModel
    An abstract base class model that provides a display field.
    """

    display = models.BooleanField(_('display'),default=False)

    class Meta:
        abstract = True