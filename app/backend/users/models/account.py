# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
    TimeStampedModel,
    ActivatorModel,
    ExternalID
)

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.managers import AccountManager 

User = get_user_model()

class Account(
    TimeStampedModel,
    ActivatorModel,
    ExternalID,
    Model
    ):

    '''
    Account
    Used for hedera account details
    This allows users to link any number of hedera wallets to a single user object
    '''

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name=_('user'),
        related_name="account_user")
    
    private_key = models.CharField(verbose_name=_('private_key'),max_length=200 )

    objects = AccountManager()
