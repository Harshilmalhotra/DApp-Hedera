# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from datetime import datetime

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase
from django.contrib.auth.hashers import make_password

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.models import CustomUser


# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status



class CustomUserTestCase(TestCase):
    """
    Test suite for CustomUser
    """
    def setUp(self):

        self.test_user = CustomUser.objects.create(
            email= "test@didcoding.com",
            first_name= "Test",
            last_name="Case",
            password= make_password("fredfred1"),
            dob= datetime.fromisoformat("1982-01-24 00:00:00+00:00")
            )


    def test_calculate_age(self):
        '''
        test the get age method
        '''
        self.assertEqual(self.test_user.calculate_age(), 41)


class SignUpTestCase(APITestCase):

    """
    Test suite for User management
    """
    def setUp(self):
        self.test_user = CustomUser.objects.create(
            email= "test@didcoding.com",
            first_name= "Test",
            last_name="Case",
            password= make_password("fredfred1"),
            dob= datetime.fromisoformat("1982-01-24 00:00:00+00:00")
            )
        self.client = APIClient()
        self.data = {
            "email": "roger@hashgraphhub.com",
            "first_name": "Roger",
            "last_name": "Redhat",
            "password": "fredfred1"
        }
        self.url = "/api/v1/auth/users/"

    def test_create_user(self):
        '''
        test djoser signup endpoint
        '''
        data = self.data
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)



class SignInTestCase(APITestCase):

    """
    Test suite for User management
    """
    def setUp(self):
        self.test_user = CustomUser.objects.create(
            email= "test@didcoding.com",
            first_name= "Test",
            last_name="Case",
            password= make_password("fredfred1"),
            dob= datetime.fromisoformat("1982-01-24 00:00:00+00:00"),
            is_active=True
            )
        self.client = APIClient()
        self.data = {
            "email": "test@didcoding.com",
            "password": "fredfred1"
        }
        self.url = "/api/v1/auth/token/login/"

    def test_login_user(self):
        '''
        test djoser signin endpoint
        '''
        data = self.data
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
