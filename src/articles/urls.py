from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path("", views.index, name="index"),
    path("article/detail/<article_id>", views.detail_article, name="detail"),
    path("article/add", views.create_article, name="add"),
    path("article/delete/<article_id>", views.delete_article, name="delete"),
    path("article/search", views.search_articles, name="search"),
    path("article/update/<int:id>", views.update_view, name="update_article"),
]
