from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post, Comment, CommentLike
from .forms import CommentForm, PostForm

# Create your views here.
class PostList (generic.ListView):
    queryset = Post.objects.filter(status=1, post_type=0)
    template_name = "blog/digging_deeper.html"
    paginate_by = 4


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
    paginator = Paginator(post_list, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated and request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.status = 1
            new_post.post_type = 1
            new_post.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Post created"
            )
        else:
            print(post_form.errors)
            messages.add_message(
                request, messages.ERROR,
                "Something went wrong, please contact admin"
            )
    else:
        post_form = PostForm()

    return render(
        request,
        "blog/diggit_forum.html",
        { "post_form": post_form,
          "page_obj": page_obj }
    )


@login_required
def edit_post(request, slug):
    """
    Allow users to edit posts created by themselves
    """
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        post_form = PostForm(data=request.POST, instance=post)

        if post.author == request.user and post_form.is_valid():
            post = post_form.save()
            messages.add_message(request, messages.SUCCESS,  'Post Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Update unsuccessful')

    return HttpResponseRedirect(reverse('read_post', args=[slug]))


@login_required
def delete_post(request, slug):
    """
    view to delete user's own post
    """
    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You cannot delete this post!')

    return HttpResponseRedirect(reverse('diggit_forum'))


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

    if request.user.is_authenticated:
        liked_comments = CommentLike.objects.filter(
            liked_by=request.user).values_list('comment_id', flat=True)
    else:
        liked_comments = []

    comments = Comment.objects.filter(post=post).top_level().ordered_by_likes()

    if request.user.is_authenticated and request.method == "POST":
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
         "comment_form": comment_form,
         "liked_comments": liked_comments,
         "comments": comments}
    )


@login_required
def edit_comment(request, slug, comment_id):
    """
    Allow users to edit posts created by themselves
    """
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_id) 
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment.author == request.user and comment_form.is_valid():
            comment = comment_form.save()
            messages.add_message(request, messages.SUCCESS,  'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Update unsuccessful')

    return HttpResponseRedirect(reverse('read_post', args=[slug]))



@login_required
def delete_comment(request, slug, comment_id):
    """
    view to delete user's own post
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You cannot delete this comment!')

    return HttpResponseRedirect(reverse('read_post', args=[slug]))


@login_required
def like_comment(request, slug, comment_id):
    """
    View to add or remove a like on a comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    queryset = CommentLike.objects.filter(comment=comment, liked_by=request.user)

    if request.method == "POST":
        if queryset.exists():
            queryset.delete()
        else:
            queryset.create(comment=comment, liked_by=request.user)

    return HttpResponseRedirect(reverse('read_post', args=[slug]))