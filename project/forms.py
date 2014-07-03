from django import forms
from django.contrib.auth.models import User
from project.models import *

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the category name.", required=True)
    image = forms.ImageField(help_text="Select an image to upload.", required=False)

    class Meta:
        model = Category
        fields = ('name', 'image')

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'price', 'date', 'category_list')

