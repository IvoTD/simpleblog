from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from .models import Post, Category

#choices = [('coding'), ('coding'), ('sports'), ('sports'), ('entertainment'), ('entertainment'),]

choices = Category.objects.all().values_list('name', ('name'))

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title tag!'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog here!'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your title tag!'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog here!'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }