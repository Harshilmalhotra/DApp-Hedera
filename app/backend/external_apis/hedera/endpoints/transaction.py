# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from external_apis.hedera import HederaBase
from external_apis.hedera import client

client = client()


class Transaction(HederaBase):
    '''
    This handles all API calls to Stripes Customer endpoint
    '''

    def __init__(self, *args, **kwargs):
        super(Transaction, self).__init__(*args, **kwargs)
        self.transaction = self.kwargs.get("transaction")
        
    @property
    def get_receipt(self):
        '''
        Used to get the transaction receipt from any Hedera object
        '''
        client = self.get_client
        obj = self.transaction.getReceipt(client)       
        return obj
    
    def get_status(self):
        '''
        Used to get the receipt status from a Hedera receipt
        '''
        receipt = self.get_receipt
        obj  = receipt.status
        return obj

