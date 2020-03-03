from django.shortcuts import render
from .models import Article, Comment, HashTag

# Create your views here.
def home(request):
    article_list = Article.objects.all()
    ctx = {
        "article_list" : article_list
    }
    return render(request, "home.html", ctx)

def detail(request):
    pass

def about(request):
    pass

