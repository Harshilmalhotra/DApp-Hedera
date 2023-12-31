# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os
import json
from datetime import datetime
import uuid


# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.gis.geos import Point


# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()


User = get_user_model()


class DBConfig:

    def manage_super_user(self)-> User:

        user = User.objects.filter(email = os.environ.get("SUPER_USER_NAME"))
        if user.exists():
            pass
        else:
            user = User.objects.create(
                email=os.environ.get("SUPER_USER_NAME"), 
                password=make_password(os.environ.get("SUPER_USER_PASSWORD")),
                first_name=os.environ.get("SUPER_USER_FIRST_NAME"),
                last_name=os.environ.get("SUPER_USER_LAST_NAME"),
                is_staff = True,
                is_active=True,
                is_superuser = True
                )
        return user

    def manage_site(self):
        site = Site.objects.first()
        site.name = "Main"
        match settings.PRODUCTION:
            case 0:
                site.domain = f"localhost:{settings.RUN_SERVER_PORT}"
            case 1:
                os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")[0]
        site.save()

    def get_object(self, name):
        name = name.split(".")
        app_name = name[0]
        model_name = name[1]
        obj = apps.get_model(app_label=app_name, model_name=model_name)
        return obj

    def create_point(self, lng, lat):
        return Point(float(lng), float(lat))
    
    def manage_kwargs(self, my_dict:dict) ->dict:
        for key, value in my_dict.items():

            match key:
                case "password":
                    pw = my_dict["password"]
                    my_dict["password"] = make_password(pw)
                case "user":
                    obj = User.objects.get(id = value)
                    my_dict[key] = obj
                
            match value:
                case "true":
                    my_dict[key] = True
                case "false":
                    my_dict[key] = False
            try:
                date_field = datetime.fromisoformat(value)
                my_dict[key] = date_field
            except (ValueError,TypeError):
                pass
        
        return my_dict



    def create_object(self, my_dict:dict):
        try:
            model = self.get_object(my_dict["model"])
            fields = self.manage_kwargs(my_dict["fields"])
            if "id" in fields.keys():
                obj = model.objects.filter(id = fields["id"])
                if obj.exists():
                    pass
                else:
                    model.objects.create(**fields)
            else:
                obj, created = model.objects.get_or_create(**fields)
            return obj
        except KeyError:
            raise Exception("'model' keyword is required")

def run():
    db_config = DBConfig()
    db_config.manage_site()
    db_config.manage_super_user()