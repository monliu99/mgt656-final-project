import os
from unittest import mock

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase

ENV = {"SEED_ADMIN_PASSWORD": "a-test-pass-1", "SEED_COUPLE1_PASSWORD": "c1-test-pass-2", "SEED_COUPLE2_PASSWORD": "c2-test-pass-3"}


class AuthTests(TestCase):
    def test_home_public(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_signup_logs_in(self):
        r = self.client.post("/signup/", {
            "username": "newlyweds", "password1": "xK9-planning-2026", "password2": "xK9-planning-2026"})
        self.assertRedirects(r, "/")
        self.assertTrue(get_user_model().objects.filter(username="newlyweds").exists())


class SeedTests(TestCase):
    def test_seed_is_idempotent_and_accounts_can_log_in(self):
        with mock.patch.dict(os.environ, ENV):
            call_command("seed")
            call_command("seed")
        self.assertEqual(get_user_model().objects.count(), 3)
        self.assertTrue(self.client.login(username="admin@example.com", password=ENV["SEED_ADMIN_PASSWORD"]))
        self.assertTrue(get_user_model().objects.get(username="admin@example.com").is_superuser)
        self.assertFalse(get_user_model().objects.get(username="couple1@example.com").is_staff)
