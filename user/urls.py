from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("inscription", views.inscription_view, name="inscription"),
    path("profil", views.profil_view, name="profil"),
    path("update/profil", views.update_profil, name="update_profil"),
    path("ad", views.my_ad_view, name="user_ad"),
]
