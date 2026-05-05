from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model): # oop (object oriented programing)
    title = models.CharField(max_length=128)  # string
    subtitle = models.CharField(max_length=256)  # string
    body = models.TextField()  # string
    created_on = models.DateTimeField(auto_now_add=True)  # date / datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )  # User model
    
    def __str__(self): # to string method
        return f"{self.id} - {self.title} by {self.author}"
    
    def get_absolute_url(self): 
        return reverse("post_detail", args=[self.id]) 
        
        