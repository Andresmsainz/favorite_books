from django.db import models
from datetime import datetime

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #1 First & Last Name should be at least 2 characters
        if len(postData['firstname']) < 5:
            errors["firstname"] = "Title is required should be at least 2 characters!"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "Last Name should be at least 2 characters!"
        #2 email already exists????  
        if len(User.objects.filter(email=postData["email"])) > 0:
            errors["email"] = "This email already exists. Please Pick Another!"
        #3 check that password and confirm password match
        if postData["password"] != postData["confirmpassword"]:
            errors["password"] = "Passwords do not match!"
        return errors

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #1 First & Last Name should be at least 2 characters
        if len(postData['title']) < 5:
            errors["title"] = "Title should be at least 2 characters!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    # liked_books = a list of books a given user likes
    # books_uploaded = a list of books uploaded by a given user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Old Book")
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded",on_delete = models.CASCADE)
    #the user who uploaded a given book
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    #a list of users who like a given book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()