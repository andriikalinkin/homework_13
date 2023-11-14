from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Blog


@cache_page(60 * 15)
def blog_view(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog.html", {"blog": blog})
