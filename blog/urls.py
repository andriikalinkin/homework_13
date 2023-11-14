from django.urls import path
from . import views


urlpatterns = [
    path("blog/", views.all_posts, name="all posts"),
    path("blog/<int:blog_id>/", views.post, name="post")
]
