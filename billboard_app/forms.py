from django.forms import ModelForm
from .models import Post
from django import forms


#creating forms from model (modelForm)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'posts_title','posts_text','posts_author', 'posts_pub_date'}
        widgets = {
        'posts_pub_date': forms.HiddenInput(),
        'posts_text': forms.Textarea(attrs={'placeholder': 'Your message here'}),
        'posts_title': forms.TextInput(attrs={'placeholder': 'Title'}),
        'posts_author': forms.TextInput(attrs={'placeholder': 'Author'})
        }


#HiddenInput