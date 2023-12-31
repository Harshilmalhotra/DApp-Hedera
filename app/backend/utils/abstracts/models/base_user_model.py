# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.fields.enums import Gender, UserTitle
from utils.validators import RegexValidator

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from enumfields import EnumField


class BaseUserModel(models.Model):

    title = EnumField(
        UserTitle,
         blank=True, 
         null=True, 
         verbose_name=_('user title'),
         max_length=100 
         )
         
    first_name = models.CharField(_('first name'),max_length=150,blank=True)
    middle_name = models.CharField(_('middle name'),max_length=150,blank=True)
    last_name = models.CharField(_('last name'),max_length=150,blank=True)

    gender = EnumField(
        Gender, 
        blank=True, 
        null=True, 
        verbose_name=_('gender'),
        max_length=100 
        )

    phone_number = models.CharField(_('phone number'),validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ], 
        max_length=17, 
        blank=True)

    class Meta:
        abstract = True