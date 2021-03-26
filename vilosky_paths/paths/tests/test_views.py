from django.test import TestCase
from paths.models import *
from django.urls import reverse
from django.contrib.auth.models import User
from paths.forms import UserForm, UserProfileForm
from paths.models import UserProfile


class RegisterPageTests(TestCase):

    def test_register_page_url(self):
        response = self.client.get("/paths/register/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="paths/register.html")

    def test_register_page_view_name(self):
        response = self.client.get(reverse("paths:register"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="paths/register.html")

    def test_register_form(self):
        user_form = UserForm(
            data={"username": "judy", "password": "pingpong1234", "email": "judy@email.com"})
        profile_form = UserProfileForm(
            data={"first_name": "Greg", "last_name": "Testy"})

        user = user_form.save()
        user.set_password(user.password)
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        self.assertTrue(user_form.is_valid())
        self.assertTrue(profile_form.is_valid())
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(len(UserProfile.objects.all()), 1)
        self.assertTrue(self.client.login(
            username="judy", password="pingpong1234"))

    def test_register_post(self):
        context = {"username": "judy", "password": "pingpong1234",
                   "email": "judy@email.com", "first_name": "Greg", "last_name": "Testy"}
        response = self.client.post(reverse("paths:register"), context)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.client.login(
            username="judy", password="pingpong1234"))


class LoginPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username="judy", first_name="Greg", last_name="Testy", email="judy@email.com")
        user.set_password("pingpong1234")
        user.save()

    def test_login_page_url(self):
        response = self.client.get("/paths/login/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="paths/login.html")

    def test_login_page_view_name(self):
        response = self.client.get(reverse("paths:login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="paths/login.html")

    def test_login_post(self):
        user = User.objects.get(id=1)
        response = self.client.post(reverse("paths:login"), {
                                    "username": "judy", "password": "pingpong1234"})

        self.assertEqual(user.id, int(self.client.session["_auth_user_id"]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("paths:dashboard"))

    def test_logged_in_present_urls(self):
        user = User.objects.get(id=1)
        self.client.login(username="judy", password="pingpong1234")
        content = self.client.get(reverse("paths:home")).content.decode()

        self.assertTrue('href="/paths/login/"' not in content)
        self.assertTrue('href="/paths/register/"' not in content)

        self.assertTrue('href="/paths/logout/"' in content)
        self.assertTrue('href="/paths/dashboard/"' in content)
        self.assertTrue('href="/paths/"' in content)
        self.assertTrue('href="/paths/search/"' in content)


class LogoutPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username="judy", first_name="Greg", last_name="Testy", email="judy@email.com")
        user.set_password("pingpong1234")
        user.save()

    def test_unlogged_logout(self):
        response = self.client.get(reverse("paths:logout"))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url, reverse("paths:login"))

    def test_logout(self):
        user = User.objects.get(id=1)
        self.client.login(username="judy", password="pingpong1234")

        self.assertEqual(user.id, int(self.client.session["_auth_user_id"]))

        response = self.client.get(reverse("paths:logout"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("paths:home"))
        self.assertTrue("_auth_user_id" not in self.client.session)

    def test_logged_out_present_urls(self):
        content = self.client.get(reverse("paths:home")).content.decode()

        self.assertTrue('href="/paths/logout/"' not in content)
        self.assertTrue('href="/paths/dashboard/"' not in content)

        self.assertTrue('href="/paths/login/"' in content)
        self.assertTrue('href="/paths/register/"' in content)
        self.assertTrue('href="/paths/"' in content)
        self.assertTrue('href="/paths/search/"' in content)
