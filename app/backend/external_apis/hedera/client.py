from django.conf import settings
#We are importing Client from the built in hedera SDK
from hedera import Client

def client():
    '''
    Used to configure the correct hedera environment
    '''
    env = settings.HEDERA_ENV
    match env:
        #Note: 'testnet' is default if nothing is passed in via .env
        case "testnet":
            return Client.forTestnet()
        case "mainnet":
            return Client.forMainnet()
        case _:
            return Client.forPreviewnet()