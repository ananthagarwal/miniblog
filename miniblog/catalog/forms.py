from django import forms
import datetime

class AddCommentForm(forms.Form):
    description = forms.CharField(max_length=2000)
    time = forms.DateTimeField(initial=datetime.date.today, disabled=True)