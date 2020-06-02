from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # model은 Post
        fields = ['title', 'author', 'body'] #사용자에게 입력받을 fields

