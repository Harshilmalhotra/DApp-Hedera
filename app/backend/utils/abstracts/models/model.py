# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import uuid

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models


class Model(models.Model):
    '''
    We use this is EVERY db entry
    '''
    id = models.UUIDField(
        _('id'),
        primary_key=True,
        default=uuid.uuid4
        )

    class Meta:
        abstract = True