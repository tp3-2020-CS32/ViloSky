from django.test import TestCase
from paths.forms import *
from paths.models import *


class UserFormTest(TestCase):

    def test_user_form(self):
        user_data = {"username": "jhudy",
                     "password": "test1234", "email": "anemail@gmail.com"}
        user_form = UserForm(data=user_data)
        self.assertTrue(user_form.is_valid())

    def test_userprofile_form(self):
        user_profile_data = {"first_name": "Jaro", "last_name": "Hudy"}
        user_profile_form = UserProfileForm(data=user_profile_data)
        self.assertTrue(user_profile_form.is_valid())
