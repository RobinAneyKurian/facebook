import imp
from django.shortcuts import render, redirect

from django.views import View

from django.contrib.auth import authenticate, login, logout

from fb.forms import UserRegistrationForm, UserLoginForm, UserProfileDetails, UploadShoppingProducts

from django.views.generic import CreateView, View, ListView, DetailView

from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django.contrib import messages

from fb.forms import UpoloadPostForm, UserProfileForm, UploadShoppingProductsForm

from fb.models import UploadPhotoVideo


class UserRegistration(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm
        return render(request, "fb_create_account.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request, "fb_create_account.html", {"form": form})

    

class FacebookLogin(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm
        return render(request, "fb_login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usr_object = authenticate(request, username=username, password=password)
            if usr_object:
                login(request, usr_object)
                return render(request, "fb_home.html")
            else:
                messages.error(request, "Invalid Credentials")
                return render(request, "fb_login.html", {"form": form})
        
class FacebookHome(ListView):
    context_object_name="files"
    model=UploadPhotoVideo
    template_name="fb_home.html"
   

    def get_queryset(self):
        return UploadPhotoVideo.objects.all()

class FacebookBase(View):
    def get(self, request, *args, **kwargs):
        return render(request, "base.html")

class FacebookUploadPostView(CreateView, ListView):
    model = UploadPhotoVideo
    template_name = "fb_upload_post.html"
    form_class = UpoloadPostForm
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"
    context_object_name = "files"

    # def post_id(request, *args, **kwargs):
    #     id = kwargs.get("id")
    #     postid = UploadPhotoVideo.objects.get(id=id)
    #     return render(request, "fb_home.html", {"id": postid})

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


def delete_post(request, *args, **kwargs):
    id = kwargs.get("id")
    UploadPhotoVideo.objects.get(id=id).delete()
    return redirect("home")

def like_view(request, *args, **kwargs):
    ans_id = kwargs.get("id")
    ans = UploadPhotoVideo.objects.get(id=ans_id)
    ans.like.add(request.user)
    ans.save()
    return redirect("home")

    

def profile_view(request, *args, **kwargs):
    return render(request ,'fb_profile.html')


class UserPostInProfile(ListView):
    context_object_name = "profilepost"
    model = UserProfileDetails
    # form_class = UserProfileForm
    template_name= "fb_profile.html"
    context_object_name = "profile"
   
   

    # def get_queryset(self):
    #     return UserProfileDetails.objects.all()

class UserProfileDetailsView(CreateView):
    model = UserProfileDetails
    form_class = UserProfileForm
    template_name = "fb_upload_profile_details.html"
    context_object_name = "form"
    success_url = reverse_lazy("profile")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return UserProfileDetails().include(user=self.request.user)


def facebook_shopping(request, *args, **kwargs):
    return render(request, "fb_shop.html")

class ShoppingProductsListView(ListView):
    model = UploadShoppingProducts
    template_name = "fb_shop.html"
    context_object_name = 'products'

    def get_queryset(self):
        return UploadShoppingProducts.objects.all()

class UploadShoppingProductsView(CreateView, ListView):
    model = UploadShoppingProducts
    form_class = UploadShoppingProductsForm
    template_name = "fb_upload_shopping_products.html"
    context_object_name = "products"
    success_url = reverse_lazy("shop")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

def LogoutSessionView(request, *args, **kwargs):
    logout(request)
    return redirect("signin")