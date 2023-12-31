# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from rest_framework import status
from rest_framework.exceptions import NotFound, APIException




class NoAccountIDException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'An Account ID was not provided'
    default_code = 'invalid'


class AccountIDDuplicationException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'The provided Account ID is already in use'
    default_code = 'invalid'