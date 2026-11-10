import re

from django.conf import settings
from django.test import Client, TestCase

from .models import Click, Impression

URL = f"/{settings.AB_HASH}"


def button_text(response):
    html = response.content.decode()
    assert html.count('id="abtest"') == 1
    return re.search(r'<button id="abtest"[^>]*>\s*(\w+)\s*</button>', html).group(1)


class HashTests(TestCase):
    def test_hash_matches_course_site_method(self):
        self.assertEqual(settings.AB_HASH, "2c65d9f")


class PageTests(TestCase):
    def test_public_200_lists_members_and_one_button(self):
        r = self.client.get(URL)
        self.assertEqual(r.status_code, 200)
        self.assertIn(button_text(r), ["kudos", "thanks"])
        for m in settings.TEAM_MEMBER_NICKNAMES:
            self.assertContains(r, m)

    def test_wrong_hash_404(self):
        self.assertEqual(self.client.get("/abcdefg").status_code, 404)

    def test_reload_counts_one_impression_and_same_variant(self):
        first = button_text(self.client.get(URL))
        for _ in range(4):
            self.assertEqual(button_text(self.client.get(URL)), first)
        self.assertEqual(Impression.objects.count(), 1)

    def test_click_counts_once_and_keeps_variant(self):
        first = button_text(self.client.get(URL))
        for _ in range(3):
            r = self.client.post(f"{URL}/click")
            self.assertRedirects(r, URL, fetch_redirect_response=False)
        self.assertEqual(Click.objects.count(), 1)
        self.assertEqual(Impression.objects.count(), 1)
        self.assertEqual(button_text(self.client.get(URL)), first)

    def test_click_without_visit_counts_nothing(self):
        self.client.post(f"{URL}/click")
        self.assertEqual(Click.objects.count(), 0)

    def test_variants_are_random_across_visitors(self):
        seen = {button_text(Client().get(URL)) for _ in range(60)}
        self.assertEqual(seen, {"kudos", "thanks"})


class StatsTests(TestCase):
    def test_preferred_is_higher_click_rate_not_count(self):
        # kudos: 10 impressions, 2 clicks (20%); thanks: 2 impressions, 1 click (50%)
        for i in range(10):
            Impression.objects.create(visitor_id=f"k{i}", variant="kudos")
        for i in range(2):
            Click.objects.create(visitor_id=f"k{i}", variant="kudos")
        for i in range(2):
            Impression.objects.create(visitor_id=f"t{i}", variant="thanks")
        Click.objects.create(visitor_id="t0", variant="thanks")
        data = self.client.get(f"{URL}/stats").json()
        self.assertEqual(data["preferred"], "thanks")
        self.assertEqual(data["kudos"], {"impressions": 10, "clicks": 2})

    def test_empty_database_still_valid(self):
        self.assertIn(self.client.get(f"{URL}/stats").json()["preferred"], ["kudos", "thanks"])
