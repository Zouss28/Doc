from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


def article_detail_view(request,id=None):
    obj=None
    if id:
        obj = Article.objects.get(id=id)
    return render(request,'articles/detail.html',{
        'obj':obj
    })
    
    
def article_search_view(request):
    # print(dir(request))
    try:
        query = int(request.GET.get('query'))
    except:
        query = None
    object = None
    if query:
        instance = Article.objects.get(id=query)
        object = instance
    return render(request, 'articles/search.html', {
        'object':object
    })
    
@login_required    
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    return render(request, 'articles/create.html', {
        'form':form
    })