from django import forms
from .models import Comment


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post","user_name","created_on"]
        labels = {
            "text": "Your comment"
        }