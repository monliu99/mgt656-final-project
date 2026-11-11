"""Create demo data and grader accounts. Safe to run repeatedly.

Passwords come from environment variables so they never live in git:
  SEED_ADMIN_PASSWORD, SEED_COUPLE1_PASSWORD, SEED_COUPLE2_PASSWORD
"""
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

ACCOUNTS = [
    ("admin@example.com", "SEED_ADMIN_PASSWORD", True),
    ("couple1@example.com", "SEED_COUPLE1_PASSWORD", False),
    ("couple2@example.com", "SEED_COUPLE2_PASSWORD", False),
]


class Command(BaseCommand):
    help = "Create (or reset) demo users used by graders. Idempotent."

    def handle(self, *args, **options):
        User = get_user_model()
        for email, env_name, is_admin in ACCOUNTS:
            password = os.environ.get(env_name)
            if not password:
                raise CommandError(f"Set the {env_name} environment variable")
            user, created = User.objects.get_or_create(
                username=email, defaults={"email": email}
            )
            user.email = email
            user.is_staff = is_admin
            user.is_superuser = is_admin
            user.set_password(password)
            user.save()
            self.stdout.write(f"{'Created' if created else 'Updated'} {email}")
