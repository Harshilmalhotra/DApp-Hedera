# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.timezone import now

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from utils.fields import  CreationDateTimeField, ModificationDateTimeField

class StatusChoices(models.IntegerChoices):

    INACTIVE_STATUS = 0
    ACTIVE_STATUS = 1
    COMING_SOON = 2
    IN_BASKET = 3
    PROCESSED = 4

class ActivatorQuerySet(models.query.QuerySet):
    """
    ActivatorQuerySet
    Query set that returns status results
    """

    def active(self):
        """ Return active query set """
        return self.filter(status=StatusChoices.ACTIVE_STATUS)

    def inactive(self):
        """ Return inactive query set """
        return self.filter(status=StatusChoices.INACTIVE_STATUS)
    
    def coming_soon(self):
        """ Return coming_soon query set """
        return self.filter(status=StatusChoices.COMING_SOON)
    
    def in_basket(self):
        """ Return in_basket query set """
        return self.filter(status=StatusChoices.IN_BASKET)
    
    def processed(self):
        """ Return processed query set """
        return self.filter(status=StatusChoices.PROCESSED)


class ActivatorModelManager(models.Manager):
    """
    ActivatorModelManager
    Manager to return instances of ActivatorModel: SomeModel.objects.active() / .inactive()
    """

    def get_queryset(self):
        """ Use ActivatorQuerySet for all results """
        return ActivatorQuerySet(model=self.model, using=self._db)

    def active(self):
        """
        Return active instances of ActivatorModel:
        SomeModel.objects.active(), proxy to ActivatorQuerySet.active
        """
        return self.get_queryset().active()

    def inactive(self):
        """
        Return inactive instances of ActivatorModel:
        SomeModel.objects.inactive(), proxy to ActivatorQuerySet.inactive
        """
        return self.get_queryset().inactive()
    
    def coming_soon(self):
        """
        Return coming_soon instances of ActivatorModel:
        SomeModel.objects.coming_soon(), proxy to ActivatorQuerySet.coming_soon
        """
        return self.get_queryset().coming_soon()
    
    def in_basket(self):
        """
        Return in_basket instances of ActivatorModel:
        SomeModel.objects.in_basket(), proxy to ActivatorQuerySet.in_basket
        """
        return self.get_queryset().in_basket()
    
    def processed(self):
        """
        Return processed instances of ActivatorModel:
        SomeModel.objects.processed(), proxy to ActivatorQuerySet.processed
        """
        return self.get_queryset().processed()




class ActivatorModel(models.Model):
    """
    ActivatorModel
    An abstract base class model that provides activate and deactivate fields.
    """

    status = models.IntegerField(_('status'), choices=StatusChoices.choices, default=StatusChoices.ACTIVE_STATUS)
    activate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for an immediate activation'))
    processed_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for an immediate activation'))
    deactivate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for indefinite activation'))
    objects = ActivatorModelManager()

    class Meta:
        ordering = ('active', '-activate_date',)
        abstract = True

    def save(self, *args, **kwargs):
        if not self.activate_date:
            self.activate_date = now()
        super().save(*args, **kwargs)