from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post, Comment, CommentLike
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """
    Display a filtered list of instances of :model:`blog.Post`

    **Context**
    ``object_list``
        A queryset of published (status=1) blog (post_type=0) posts,
        paginated by 4.

    **Template**
    :template:`blog/digging_deeper.html`
    """
    queryset = Post.objects.filter(status=1, post_type=0)
    template_name = "blog/digging_deeper.html"
    paginate_by = 4


def forum_list(request):
    """
    Display a filtered list of instances of :model:`blog.Post`

    **Context**
    ``page_obj``
        A paginated list of 6 instances of :model:`blog.Post`
    ``post_form``
        An instance of :form:`PostForm`

    **Template**
    :template:`blog/diggit_forum.html`
    """
    post_list = Post.objects.filter(status=1, post_type=1)
    paginator = Paginator(post_list, 6)

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
            post_form.save_m2m()  # To save the categories
            messages.add_message(
                request, messages.SUCCESS,
                "Post created"
            )
            return HttpResponseRedirect(
                reverse('read_post', args=[new_post.slug]))
        else:
            return render(
                request,
                "blog/diggit_forum.html",
                {"post_form": post_form,
                    "page_obj": page_obj}
            )
    else:
        post_form = PostForm()

    return render(
        request,
        "blog/diggit_forum.html",
        {"post_form": post_form,
            "page_obj": page_obj}
    )


@login_required
def edit_post(request, slug):
    """
    Allow users to edit instances of :model:`blog.Post` created by
    themselves.

    **Context**
    ``post``
        The forum post that the user is editing
    ``post_form``
        An instance of :form:`PostForm`, pre-populated with existing
        post data

    **Template**
    :template:`blog/read_post.html` for successful edits
    :template:`blog/diggit_forum.html` for unsuccessful edits
    """
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        messages.add_message(
            request, messages.ERROR,
            'You can only edit your own posts.'
        )
        return redirect('diggit_forum')
    
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid():
            post = post_form.save()
            messages.add_message(request, messages.SUCCESS, 'Post Updated!')
            return HttpResponseRedirect(reverse('read_post', args=[slug]))
        else:
            messages.add_message(
                request, messages.ERROR, 'Update Unsuccessful')
    else:
        post_form = PostForm()

    return redirect('diggit_forum')


@login_required
def delete_post(request, slug):
    """
    Allow users to delete instances of :model:`blog.Post` created by
    themselves.

    **Template**
    Redirects to :template:`blog/diggit_forum.html`
    """
    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You cannot delete this post!')

    return redirect('diggit_forum')


def home_page(request):
    """
    Renders the homepage

    **Template**
    :template:`home.html`
    """
    return render(request, 'home.html')


def read_post(request, slug):
    """
    Display a single instance of :model:`blog.Post`
    Display all comments relating to the post instance
    Allow users to create instances of :model:`blog.Comment`

    **Context**
    ``post``
        An instance of :model:`blog.Post`
    ``comment_form``
        An instance of :form:`CommentForm`
    ``liked_comments``
        List of comments liked by the user
    ``comments``
        List of top-level comments relating to this post ordered
        by number of likes then date

    **Template**
    :template:`blog/read_post.html`
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
            return HttpResponseRedirect(reverse('read_post', args=[slug]))

        else:
            messages.add_message(
                request, messages.ERROR, 'Something went wrong'
            )
            return render(
                request,
                "blog/read_post.html",
                {"post": post,
                    "liked_comments": liked_comments,
                    "comments": comments,
                    "comment_form": comment_form}
            )
    else:
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
    Allow users to edit instances of :model:`blog.Comment` created by
    themselves.

    **Template**
    Redirects to :template:`blog/read_post.html`
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author != request.user:
        messages.add_message(
            request, messages.ERROR,
            'You can only edit your own comments.'
        )
        return HttpResponseRedirect(reverse('read_post', args=[slug]))
   
    if request.method == "POST":
        
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment = comment_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Update unsuccessful')

    return HttpResponseRedirect(reverse('read_post', args=[slug]))


@login_required
def delete_comment(request, slug, comment_id):
    """
    Allow users to delete instances of :model:`blog.Comment` created by
    themselves.

    **Template**
    Redirects to :template:`blog/read_post.html`
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You cannot delete this comment!')

    return HttpResponseRedirect(reverse('read_post', args=[slug]))


@login_required
def like_comment(request, slug, comment_id):
    """
    Allow users to create/delete instances of :model:`blog.CommentLike`

    **Template**
    Redirects to :template:`blog/read_post.html`
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    queryset = CommentLike.objects.filter(
        comment=comment, liked_by=request.user)

    if request.method == "POST":
        if queryset.exists():
            queryset.delete()
        else:
            queryset.create(comment=comment, liked_by=request.user)

    return HttpResponseRedirect(reverse('read_post', args=[slug]))
