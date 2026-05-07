from django.urls import path
from .views import (
    PostDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete")
]