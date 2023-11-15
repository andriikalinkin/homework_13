from django.urls import path
from . import views


urlpatterns = [
    path("blog/", views.posts, name="all posts"),
    path("blog/<int:blog_id>/", views.post, name="post"),
]
