# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
    BaseUserModel,
    CalculateAgeMixin, 
    TimeStampedModel
)
from utils.validators import RegexValidator

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.managers import CustomUserManager


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<email>/<filename>
    return f'{instance.email}/{filename}'


#This is the new custom user model
class CustomUser(AbstractBaseUser, BaseUserModel , TimeStampedModel,CalculateAgeMixin, Model, PermissionsMixin):

    '''
    CustomUser
    This is our custom user model.
    We are extending the built-in User model in Django.
    '''

    email = models.EmailField(_('email address'),unique=True)
    image = models.ImageField(_('image'),upload_to=user_directory_path, default="default_avatar.jpg")
    dob = models.DateTimeField(_('date of birth'),blank=True,null=True)
    about = models.TextField(_('about'),max_length=500,blank=True)
    phone_number = models.CharField(_('phone number'),validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ], 
        max_length=17, 
        blank=True)
    
    groups = models.ManyToManyField(Group,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()

