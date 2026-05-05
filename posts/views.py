# from django.shortcuts import render

# Create your views here.
from django.views.generic import (ListView)
from .models import Post

class PostListView(ListView):
    # template_name is the attribute to render the html
    # Specifies the template to render.
    template_name = "post/list.html"
    # Specifies the model to retrieve data from.
    model = Post

    # Sets the context variable name for the template.
    context_object_name = "posts"