from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect, render

from articles.models import Article
from team.models import Member

"""
All the views in this project are in this file.
Since the project is really simple, I have decided against splitting the URLs
into different apps.
"""

def home(request):
    return render(request, "index.html")

def about(request):
    # Gets all members via alphabetical order on name
    team = Member.objects.all().order_by("name")
    return render(request, "about.html", {"team": team})

def articles(request):
    articles = Article.objects.all().order_by("date").reverse()
    return render(request, "articles.html", {"articles": articles})

def article(request, id):
    article = Article.objects.get(pk=int(id))
    return render(request, "article.html", {"article": article})

def write(request):
    return render(request, "write.html")