# The app-level URLConf handling ALL URLs (except /admin/), because the
# project-level urls.py forwards every request with an empty prefix ("")
# directly to this file.
from django.urls import path

from my_site import views as my_site_views

from . import views


urlpatterns = [
    # Handling localhost:8000/  (the homepage):
    path("", my_site_views.homepage, name="homepage"),
    # Handling localhost:8000/posts/  URL:
    path("posts/", views.index, name="index"),
    # Handling individual posts URLs using one Dynamic path:
    path("posts/<slug:slug>", views.post_detail, name="post_detail"),
]
