from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Articles, Town, Category
from user.models import Account
from .forms import ArticleForm


def is_valid_queryparam(param):
    return param != "" and param is not None


def index(request):
    context = {}
    articles = Articles.objects.all()
    category = Category.objects.all()
    town = Town.objects.all()
    context["category"] = category
    context["town"] = town

    article_name = request.GET.get("article_name")
    article_category = request.GET.get("article_category")
    article_town = request.GET.get("article_town")

    if is_valid_queryparam(article_category):
        articles = articles.filter(category=article_category)
    if is_valid_queryparam(article_town):
        articles = articles.filter(town=article_town)
    if is_valid_queryparam(article_name):
        article_list = article_name.split(" ")
        articles = articles.filter(title__in=article_list)

    context["articles"] = articles.order_by("-timestamp")

    return render(request, "articles/index.html", context)


def detail_article(request, article_id):
    article = get_object_or_404(Articles, id=article_id)

    return render(request, "articles/detail_article.html", {"article": article})


@login_required(login_url="/user/login")
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


@login_required(login_url="/user/login")
def delete_article(request, article_id):
    if request.method == "POST":
        obj = get_object_or_404(Articles, id=article_id)
        obj.delete()
        return redirect("user_ad")

    return render(request, "user/ad.html", {})


def search_articles(request):
    context = {}
    articles = Articles.objects.all()
    category = Category.objects.all()
    town = Town.objects.all()
    context["category"] = category
    context["Town"] = town

    article_name = request.GET.get("article_name")
    article_category = request.GET.get("article_category")
    article_town = request.GET.get("article_town")

    return render(request, "articles/index.html", context)
