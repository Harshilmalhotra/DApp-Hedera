# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import datetime

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.gis.db import models
from django.utils import timezone


class CalculateAgeMixin(models.Model):

    def calculate_age(self):
        born = self.dob
        today = timezone.now().date()

        try:
            birthday = born.replace(year = today.year)
    
        # raised when birth date is February 29
        # and the current year is not a leap year
        except ValueError:
            birthday = born.replace(year = today.year,
                    month = born.month + 1, day = 1)
    
        if birthday.date() > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year

    class Meta:
        abstract = True
