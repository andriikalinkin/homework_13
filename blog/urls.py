from django.urls import path
from . import views


urlpatterns = [path("blog/<int:blog_id>/", views.blog_view, name="blog")]
