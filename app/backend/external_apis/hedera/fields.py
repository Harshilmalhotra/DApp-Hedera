# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from enumfields import Enum
from datetime import datetime
import logging

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from rest_framework.exceptions import ValidationError
from rest_framework_json_api.serializers import ChoiceField, UUIDField as DefaultUUIDField, CharField
from rest_framework_json_api.relations import ResourceRelatedField
from rest_framework import serializers



logger = logging.getLogger(__name__)


class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """

    def to_representation(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """

        converted = datetime.fromtimestamp(float('%s' % (int(value) / 1000))) if value else None
        return super(TimestampField, self).to_representation(converted)

    def to_internal_value(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        result = super(TimestampField, self).to_internal_value(value)
        logger.info("RESULT=%r" % result)
        return result.timestamp()


