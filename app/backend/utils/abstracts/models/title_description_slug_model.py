# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.abstracts import TitleDescriptionModel
from utils.fields import AutoSlugField


class TitleSlugDescriptionModel(TitleDescriptionModel):
    """
    TitleSlugDescriptionModel
    An abstract base class model that provides title and description fields
    and a self-managed "slug" field that populates from the title.
    .. note ::
        If you want to use custom "slugify" function, you could
        define ``slugify_function`` which then will be used
        in :py:class:`AutoSlugField` to slugify ``populate_from`` field.
        See :py:class:`AutoSlugField` for more details.
    """

    slug = AutoSlugField(_('slug'), populate_from='title')

    class Meta:
        abstract = True