from django.urls import path

from . import views

urlpatterns = [
    path("<str:ab_hash>", views.page, name="abtest-page"),
    path("<str:ab_hash>/click", views.click, name="abtest-click"),
    path("<str:ab_hash>/stats", views.stats, name="abtest-stats"),
]
