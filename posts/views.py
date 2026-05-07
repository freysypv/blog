# from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class PostListView(ListView): # GET requestto dysplay a liust of posts
    # template_name is the attribute to render the html
    # Specifies the template to render.
    template_name = "post/list.html"
    # Specifies the model to retrieve data from.
    model = Post

    # Sets the context variable name for the template.
    context_object_name = "posts"


class PostDetailView(DetailView): # GET Request -> single element (object)
    template_name = "post/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): # POST request -> create a new element (object)
    template_name = "post/new.html"
    model = Post
    #fields attribute is a list that allow ius to enable/disable the inputs to reder in the form
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")  # redirect to the list of posts after deleting a post
    