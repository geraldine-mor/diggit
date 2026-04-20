from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
class PostList (generic.ListView):
    queryset = Post.objects.filter(status=1, post_type=0)
    template_name = "blog/digging_deeper.html"


def forum_list (request):
    """
    Display a filtered list of instances of :model: `blog.Post`

    **Context**
    ``post``
        An instance of :model: `blog.post`
    ``post_form`` 
        The form to add a post    

    **Template**
    :template: blog/diggit_forum.html
    """
    post_list = Post.objects.filter(status=1, post_type=1)

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.status = 1
            new_post.post_type =1
            new_post.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Post created"
            )

    post_form = PostForm()

    return render(
        request,
        "blog/diggit_forum.html",
        { "post_list": post_list,
         "post_form": post_form }
    )

def home_page(request):
    return render(request, 'home.html')


def read_post(request, slug):
    """
    Display a single instance of :model: `blog.Post`

    **Context**
    ``post``
        An instance of :model: `blog.post`
    ``comment_form`` 
        The form to add a comment    

    **Template**
    :template: blog/read_post.html
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_id = request.POST.get('parent_id')
            
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=int(parent_id))

            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment saved"
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/read_post.html",
        {"post": post,
         "comment_form": comment_form}
    )
