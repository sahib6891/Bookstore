from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Category.models import *


class BookForm(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    publisher = forms.CharField(max_length=50)
    language = forms.CharField(max_length=50)
    year = forms.DateField()
    rating_user = forms.FloatField()
    price = forms.FloatField()


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author_fname', 'author_lname', 'rating_user']
form = AuthorForm()

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username','password']

# class UserForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)

