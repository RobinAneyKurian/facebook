import imp
from django import forms 
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from fb.models import UploadPhotoVideo, UserProfileDetails, UploadShoppingProducts

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ["first_name", "last_name", "username", "email", "password"]

        widgets = {
            "first_name" : forms.TextInput(attrs={"class": "form-control", "placeholder": "Firstname"}),
            "last_name" : forms.TextInput(attrs={"class": "form-control", "placeholder": "Lastname"}),
            "email" : forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "username" : forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password" : forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control", "border": "solid red 3px"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))

class UpoloadPostForm(forms.ModelForm):
    class Meta:
        model = UploadPhotoVideo
        fields = ["images", "description"]

        widgets = {

            "description": forms.Textarea(attrs={"class":"form-control", "placeholder": "Description", "col": 3,}),
            "images": forms.FileInput(attrs={"class": "form-select"})
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileDetails
        fields = ['profile_background_image', 'profile_image']

        widgets = {
            "profile_background_image": forms.FileInput(attrs={"class": "form-select"}),
            "profile_image": forms.FileInput(attrs={"class": "form-select"})
        }


class UploadShoppingProductsForm(forms.ModelForm):
    class Meta:
        model = UploadShoppingProducts
        fields = ["description", "price", "stock", "product_image"]

        widgets = {
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "product_image": forms.FileInput(attrs={"class": "select-form"})
        }

        