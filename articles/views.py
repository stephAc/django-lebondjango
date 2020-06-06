from django.shortcuts import render, get_object_or_404, redirect

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
    confirmation = False
    context = {}

    if request.POST:
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.save()
            form = ArticleForm()
            confirmation = True
    else:
        form = ArticleForm()

    context["form"] = form
    context["confirmation"] = confirmation

    return render(request, "articles/create_article.html", context)


def delete_article(request, article_id):
    if request.method == "POST":
        obj = get_object_or_404(Articles, id=article_id)
        obj.delete()
        return redirect("user_ad")

    return render(request, "user/ad.html", {})
