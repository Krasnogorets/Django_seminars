import datetime

from django import forms
from .models import Author, Article,Comment


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    secondname = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    birthday = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


class AuthorForm1(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'secondname', 'email', 'bio', 'birthday']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        authors = Author.objects.values('name')
        author = forms.ChoiceField(choices=([authors]))
        published = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
        fields = ['title', 'text', 'author', 'category','published']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        authors = Author.objects.values('name')
        author = forms.ChoiceField(choices=([authors]))
        fields = ['comment','author']