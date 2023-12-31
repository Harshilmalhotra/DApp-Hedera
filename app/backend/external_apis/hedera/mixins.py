# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from external_apis.hedera import client

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from hedera import (
    PrivateKey,
    AccountId,
    Hbar,
)


client = client()


class HederaBase:
    '''
    Base methods for Hedera api calls
    '''

    def __init__ (self, *args, **kwargs):
        self.account_id = kwargs.get("account_id")
        self.operator = kwargs.get("operator", settings.HEDERA_OPERATOR_ID)
        self.operator_key = kwargs.get("operator_key", settings.HEDERA_OPERATOR_KEY)
        self.operator_private_key = kwargs.get("operator_private_key", settings.HEDERA_OPERATOR_PRIVATE_KEY)

    @property
    def get_client(self):
        '''
        Used to create a client object to sign transactions
        '''
        operator = self.get_str_repr_object(AccountId, self.operator)
        operator_private_key = self.get_str_repr_object(PrivateKey, self.operator_private_key)
        set_operator = client.setOperator(operator, operator_private_key)
        return set_operator

    @property
    def create_private_key(self)->PrivateKey:
        '''
        Used to create a new private key
        '''
        return PrivateKey.generate()
    
    def get_public_key(self, key)->str:
        '''
        Used to get public key from privatekey
        '''
        return key.getPublicKey()
    
    def get_object_str_repr(self, obj)->str:
        '''
        Used to convert a Hedera object to str repr
        '''
        return obj.toString()
    
    def get_str_repr_object(self, obj, str):
        '''
        Used to convert str repr to Hedera obj
        '''
        if obj == Hbar:
            return obj.fromTinybars(str)
        return obj.fromString(str)