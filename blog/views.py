from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Blog


@cache_page(60)
def posts(request):
    all_posts = Blog.objects.all()
    return render(request, "all_posts.html", {"all_posts": all_posts})


@cache_page(60)
def post(request, blog_id: int):
    one_post = get_object_or_404(Blog, id=blog_id)
    return render(request, "post.html", {"one_post": one_post})
