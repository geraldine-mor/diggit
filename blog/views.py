from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment

# Create your views here.
class PostList (generic.ListView):
    # Need to filter this to blog 
    # posts only when Forum posts are an option
    queryset = Post.objects.filter(status=1)
    template_name = "digging_deeper.html"


def home_page(request):
    return render(request, 'home.html')


def read_post(request, slug):
    """
    Display a single instance of :model: `blog.Post`

    **Context**
    ``post``
        An instance of :model: `blog.post`

    **Template**
    :template: blog/read_post.html
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/read_post.html",
        {"post": post}
    )
