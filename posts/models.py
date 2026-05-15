from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    class Meta:
        verbose_name_plural = "status"

    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=200, help_text="Write a descrition about the status")

    def __str__(self):
        return f"{self.name}"



class Post(models.Model): # oop (object oriented programing)
    title = models.CharField(max_length=128)  # string
    subtitle = models.CharField(max_length=256)  # string
    body = models.TextField()  # string
    created_on = models.DateTimeField(auto_now_add=True)  # date / datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )  # User model

    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING
    )

    
    
    def __str__(self): # to string method
        return f"{self.id} - {self.title} by {self.author}"
    
    def get_absolute_url(self): # Redirect a user when we executer a Post request
        return reverse("post_detail", args=[self.id]) 
    

        
        