from django.urls import path

from . import views

urlpatterns = [
    path("authentication", views.authentication_view, name="authentication"),
    path("inscription", views.inscription_view, name="inscription"),
]
