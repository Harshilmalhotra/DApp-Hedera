# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _


# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from external_apis.hedera import HederaBase

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from rest_framework import serializers
from rest_framework.fields import DateField
from rest_framework_json_api.serializers import SerializerMethodField
from jsonapi_client.resourceobject import ResourceObject

class GetAccountInfoSerializer(HederaBase, serializers.Serializer):
    '''
        { 
            accountId=0.0.96928, 
            contractAccountId=0000000000000000000000000000000000017aa0, 
            "deleted=false", 
            "proxyAccountId=null", //deprecated
            proxyReceived=0 tℏ, //deprecated
            key=302a300506032b65700321001a5a62bb9f35990d3fea1a5bb7ef6f1df0a297697adef1e04510c9d4ecc5db3f, 
            balance=1 ℏ, 
            sendRecordThreshold=92233720368.54775807 ℏ,
            receiveRecordThreshold=9223372 0368.54775807 ℏ, 
            "receiverSignatureRequired=false",
            expirationTime=2021-02-02T19:29:36Z, 
            autoRenewPeriod=PT2160H, 
            liveHashes="[],
            tokenRelationships={ //deprecated
                0.0.27335=TokenRelationship{
                    tokenId=0.0.27335, symbol=F, balance=5, kycStatus=null,
                    freezeStatus=null, automaticAssociation=true
                } 
            },
            accountMemo=, 
            ownedNfts=0,
            maxAutomaticTokenAssociations=10
            ledgerId=previewnet
        }
    '''

    def __init__(self, *args, **kwargs):
        super(GetAccountInfoSerializer, self).__init__(*args, **kwargs)

    accountId = SerializerMethodField()
    contractAccountId = SerializerMethodField()
    key = SerializerMethodField()
    balance = SerializerMethodField()
    sendRecordThreshold = SerializerMethodField()
    receiveRecordThreshold = SerializerMethodField()

    def get_accountId(self, resource: ResourceObject) -> str:
        return self.get_account_id_str(resource.accountId)
    
    def get_contractAccountId(self, resource: ResourceObject) -> str:
        return self.get_account_id_str(resource.contractAccountId)
    
    def get_balance(self, resource: ResourceObject) -> str:
        return self.get_hbar_str(resource.balance)
    
    def get_sendRecordThreshold(self, resource: ResourceObject) -> str:
        return self.get_hbar_str(resource.sendRecordThreshold)
    
    def get_receiveRecordThreshold(self, resource: ResourceObject) -> str:
        return self.get_hbar_str(resource.receiveRecordThreshold)
    

    def validate(self,data):
        return data
    

