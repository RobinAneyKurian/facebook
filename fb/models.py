from django.db import models

from django.contrib.auth.models import User

class UploadPhotoVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 5000000)
    like = models.ManyToManyField(User, related_name="like")
    images = models.ImageField(upload_to = "images", null=True)
    posted_date = models.DateField(auto_now_add=True)

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfileDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_background_image = models.ImageField(upload_to = "profile_background_image", null=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True)
    user_followers = models.ManyToManyField(User, related_name="followers")

class UploadShoppingProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="product_images", null=True)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
