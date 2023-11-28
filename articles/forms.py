from typing import Any
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        
    def clean_title(self) :
        return "The future is now"
        
        