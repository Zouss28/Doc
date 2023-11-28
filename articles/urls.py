from django.urls import path
from .views import article_detail_view, article_create_view,article_search_view

urlpatterns = [
    path('',article_search_view),    
    path('create',article_create_view),
    path('<int:id>',article_detail_view), 
]
