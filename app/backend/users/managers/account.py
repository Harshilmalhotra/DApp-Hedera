# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import ActivatorModelManager
from django.contrib.auth.hashers import make_password as encrypt_key



class AccountManager(ActivatorModelManager):

    def create_account(self, user, external_id, public_key, private_key, **kwargs):
        '''
        Apply Django built in hasher to keys
        '''
        account = self.model(user=user, external_id=external_id, **kwargs)
        account.public_key = encrypt_key(public_key)
        account.private_key = encrypt_key(private_key)
        account.save()
        return account