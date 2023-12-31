# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.abstracts import RichTextModel


class TitleDescriptionModel(RichTextModel):
    """
    TitleDescriptionModel
    An abstract base class model that provides title and description fields.
    """

    title = models.CharField(_('title'), max_length=255)

    class Meta:
        abstract = True