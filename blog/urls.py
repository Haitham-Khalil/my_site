# Defining URLs that start with localhost:8000/posts.
from django.urls import path

from . import views


urlpatterns = [
    # Handling localhost:8000/posts/  URL:
    path("", views.index, name="index"),
    # Handling individual posts URLs using one Dynamic path:
    path("<slug:slug>", views.post_detail, name="post_detail"),
]
