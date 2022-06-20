from . models import Comment
from django import forms

class SearchForm(forms.Form):
    search_post = forms.CharField(max_length=50)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        
