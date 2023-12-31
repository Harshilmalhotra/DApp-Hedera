# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from ckeditor.fields import RichTextField


class RichTextModel(models.Model):
    """
    RichTextModel

    An abstract base class model that provides self-managed "description" and "summary" field
    using ck_editor.
    """
    description = RichTextField(
        _('description'),
        blank=True,
        null=True
        )
    
    description_summary = RichTextField(
        _('summary'),
        blank=True,
        null=True
        )
    
    summary = RichTextField(
        _('summary'),
        blank=True,
        null=True
        )
        
    class Meta:
        abstract = True