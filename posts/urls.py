from django.urls import path
from .views import (
    PostDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostArchivedListView,
    PostDraftListView
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("archived", PostArchivedListView.as_view(), name="post_archived"),
    path("drafts", PostDraftListView.as_view(), name="post_drafts"),
]