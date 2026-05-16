# from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,  #make that the user has to login to see and do
    UserPassesTestMixin
)

class PostListView(ListView): # GET requestto dysplay a liust of posts
    # template_name is the attribute to render the html
    # Specifies the template to render.
    template_name = "post/list.html"
    # Specifies the model to retrieve data from.
    # model = Post
    # Sets the context variable name for the template.
    published_status = Status.objects.get(name="published")
    #queryset attribute allow us to seclet data from the db using the model class
    # and also allow us to custmize the data (filter)
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    #context_object_name attribute allow us to change the
    #varieble on how we call it inside of templates
    context_object_name = "posts"  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_status"] = "All"       
        return context
    
class PostArchivedListView(ListView):  
    template_name = "post/list.html"
    archived_status = Status.objects.get(name="archived")
    queryset = Post.objects.filter(status=archived_status)
    context_object_name="posts" 

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["post_status"] = "Archived"
        return context
    
class PostDraftListView(ListView):
    template_name = "post/list.html"
    context_object_name="posts"

    def get_queryset(self):
        draft_status = Status.objects.get(name="draft")
        return Post.objects.filter(status=draft_status)
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["post_status"] = "Drafts"
        return context
 

class PostDetailView(LoginRequiredMixin, DetailView): # GET Request -> single element (object)
    template_name = "post/detail.html"
    model = Post
    context_object_name = "single_post"
      

class PostCreateView(LoginRequiredMixin, CreateView): # POST request -> create a new element (object)
    template_name = "post/new.html"
    model = Post
    #fields attribute is a list that allow ius to enable/disable the inputs to reder in the form
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]
    

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                 return True
            else:
                return False
        else:
            return False
        
        # print(f"printing post {post}")
        # print(f"printing request:(self.request)")
        # print(f"printing self: {self}")

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")  # redirect to the list of posts after deleting a post
    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                 return True
            else:
                return False
        else:
            return False