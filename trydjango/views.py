from django.shortcuts import render
from articles.models import Article

def home_view(request):
    instance = Article.objects.all()
    return render(request,"home_view.html",{
        "obj_list":instance
    })