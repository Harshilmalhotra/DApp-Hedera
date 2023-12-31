# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from typing import Dict
import logging

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings
from django.core.exceptions import  ValidationError


# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from rest_framework.exceptions import ValidationError as DRFValidationError


logger = logging.getLogger(__name__)


class BaseMetadataValidator(object):

    def __init__(self):

        self.MAX_METADATA_LENGTH = settings.MAX_METADATA_LENGTH
        self.MAX_METADATA_KEY_LENGTH = settings.MAX_METADATA_KEY_LENGTH
        self.MAX_METADATA_VALUE_LENGTH = settings.MAX_METADATA_VALUE_LENGTH

        self.validate_size_error_message = "The 'metadata' field size exceeded. Maximum keys count is %s."
        self.validate_key_length_error_message = "The key: %s. Allowed symbols length exceeded. Maximum is %s."
        self.validate_value_length_error_message = "The value: %s. Allowed symbols length exceeded. Maximum is %s."

    def __call__(self, value):
        self._validate_metadata(value)



class DRFMetadataValidator(BaseMetadataValidator):
    

    def _validate_metadata(self, value) -> None:
        """
        This function validates metadata.
        Metadata must be received a key, value pairs.
        We also validate key count, key length and value length.
        :param value:
        :return:
        """
        errors = []

        value_type = type(value)

        if value_type is dict:
            # Validate keys count
            if len(value) > self.MAX_METADATA_LENGTH:
                errors.append(DRFValidationError(self.validate_size_error_message % self.MAX_METADATA_LENGTH))
            # Validate characters length
            for key in value:
                if len(str(key)) > self.MAX_METADATA_KEY_LENGTH:
                    errors.append(
                        DRFValidationError(self.validate_key_length_error_message % (key, self.MAX_METADATA_KEY_LENGTH)))
                if len(str(value[key])) > self.MAX_METADATA_VALUE_LENGTH:
                    errors.append(
                        DRFValidationError(
                            self.validate_value_length_error_message % (value[key], self.MAX_METADATA_VALUE_LENGTH)))
        else:
            errors.append(DRFValidationError("metadata field must be a key, value pair."))
            
        if errors:
            raise DRFValidationError(errors)




class MetadataValidator(BaseMetadataValidator):


    def _validate_metadata(self, value) -> None:
        """
        This function validates metadata.
        Metadata must be received a key, value pairs.
        We also validate key count, key length and value length.
        :param value:
        :return:
        """
        errors = []

        value_type = type(value)

        if value_type is dict:
            # Validate keys count
            if len(value) > self.MAX_METADATA_LENGTH:
                errors.append(ValidationError(self.validate_size_error_message % self.MAX_METADATA_LENGTH))
            # Validate characters length
            for key in value:
                if len(str(key)) > self.MAX_METADATA_KEY_LENGTH:
                    errors.append(
                        ValidationError(self.validate_key_length_error_message % (key, self.MAX_METADATA_KEY_LENGTH)))
                if len(str(value[key])) > self.MAX_METADATA_VALUE_LENGTH:
                    errors.append(
                        ValidationError(
                            self.validate_value_length_error_message % (value[key], self.MAX_METADATA_VALUE_LENGTH)))
        else:
            errors.append(ValidationError("metadata field must be a key, value pair."))
            
        if errors:
            raise ValidationError(errors)

