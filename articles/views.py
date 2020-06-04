from django.shortcuts import render, get_object_or_404

from .models import Articles, Town, Category
from .forms import ArticleForm


def index(request):
    articles = Articles.objects.all()

    return render(request, "articles/index.html", {"articles": articles})


def detail_article(request, article_id):
    # article = Articles.objects.get(id=article_id)
    article = get_object_or_404(Articles, id=article_id)

    return render(request, "articles/detail_article.html", {"article": article})


def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("save")

    return render(request, "articles/create_article.html", {"form": form})


def delete_article(request, article_id):
    if request.method == "DELETE":
        obj = get_object_or_404(Articles, id=article_id)
        obj.delete()
        return redirect(request, "pages/home.html", {})

    return render(request, "pages/home.html", {})
