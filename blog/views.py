from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList (generic.ListView):
    # Need to filter this to blog 
    # posts only when Forum posts are an option
    queryset = Post.objects.filter(status=1)
    template_name = "digging_deeper.html"


def home_page(request):
    return render(request, 'home.html')