from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Blog


def all_posts(request):
    posts = Blog.objects.all()
    return render(request, "all_posts.html", {"posts": posts})


# @cache_page(60 * 15)
def post(request, blog_id: int):
    post = get_object_or_404(Blog, id=blog_id)
    return render(request, "post.html", {"post": post})
