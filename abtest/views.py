import random
import uuid

from django.conf import settings
from django.db import IntegrityError
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import VARIANTS, Click, Impression

SESSION_KEY = "abtest_visitor"


def _check_hash(ab_hash):
    if ab_hash != settings.AB_HASH:
        raise Http404


def _get_impression(request):
    visitor_id = request.session.get(SESSION_KEY)
    if visitor_id:
        return Impression.objects.filter(visitor_id=visitor_id).first()
    return None


def page(request, ab_hash):
    _check_hash(ab_hash)
    impression = _get_impression(request)
    if impression is None:
        visitor_id = str(uuid.uuid4())
        impression = Impression.objects.create(
            visitor_id=visitor_id, variant=random.choice(VARIANTS)
        )
        request.session[SESSION_KEY] = visitor_id
    return render(
        request,
        "abtest/page.html",
        {
            "variant": impression.variant,
            "members": settings.TEAM_MEMBER_NICKNAMES,
            "click_url": f"/{settings.AB_HASH}/click",
        },
    )


@require_POST
def click(request, ab_hash):
    _check_hash(ab_hash)
    impression = _get_impression(request)
    if impression is not None:
        try:
            Click.objects.get_or_create(
                visitor_id=impression.visitor_id,
                defaults={"variant": impression.variant},
            )
        except IntegrityError:
            pass  # concurrent double-click: already counted
    return redirect("abtest-page", ab_hash=settings.AB_HASH)


def _counts(variant):
    return {
        "impressions": Impression.objects.filter(variant=variant).count(),
        "clicks": Click.objects.filter(variant=variant).count(),
    }


def stats(request, ab_hash):
    _check_hash(ab_hash)
    data = {v: _counts(v) for v in VARIANTS}

    def rate(v):
        imp = data[v]["impressions"]
        return data[v]["clicks"] / imp if imp else 0.0

    # Ties (including no data) resolve to "kudos".
    data["preferred"] = "thanks" if rate("thanks") > rate("kudos") else "kudos"
    return JsonResponse(data)
