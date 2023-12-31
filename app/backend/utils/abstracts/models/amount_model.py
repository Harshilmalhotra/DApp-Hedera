# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from djmoney.models.fields import MoneyField


class AmountModel(models.Model):
    """
    UserModel
    An abstract base class model that provides an amount money field to a model
    """

    amount = MoneyField(
        _("amount"),
        max_digits=14, 
        decimal_places=2, 
        default_currency='GBP', 
        null=True, 
        blank=True)

    class Meta:
        abstract = True