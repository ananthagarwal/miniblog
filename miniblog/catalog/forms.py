from django import forms
from django.forms import ModelForm
from .models import Blog
import datetime

class AddCommentForm(forms.Form):
    description = forms.CharField(max_length=2000, widget=forms.Textarea)
    time = forms.DateTimeField(initial=datetime.date.today, disabled=True)

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'post']