from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("pages.urls")),
    path("ad/", include("articles.urls")),
    path("user/", include("user.urls")),
    path("admin/", admin.site.urls),
]
