from django.db import models

VARIANTS = ["kudos", "thanks"]


class Impression(models.Model):
    """One row per visitor, created the first time they see the page."""

    visitor_id = models.CharField(max_length=36, unique=True)
    variant = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Click(models.Model):
    """At most one row per visitor."""

    visitor_id = models.CharField(max_length=36, unique=True)
    variant = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
