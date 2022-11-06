from django.db.models import Q
from .models import BlogPost, BlogComment
from django.contrib.auth.decorators import login_required
from .forms import BlogpostForm, BlogCommentForm
from django.shortcuts import (render, redirect, reverse, get_object_or_404)
from django.contrib import messages


def blog(request):
    """
    Show blogs and search for blogs by title or content
    """
    blogposts = BlogPost.objects.all()
    query = None

    # Search function for blog if the user has made a search request
    if 'query' in request.GET:
        query = request.GET['query']

        # Search without entering request
        if not query:
            messages.error(request, "No search criteria entered")
            return redirect(reverse('blog'))
        queries = Q(
                title__icontains=query) | Q(content__icontains=query)
        blogposts = blogposts.filter(queries)

    context = {
        'blogposts': blogposts,
        'search_term': query,
    }

    return render(request, 'blog/blog.html', context)


def blog_details(request, blogpost_id):
    """
    A view to show blogpost details with content text, and add comments to them
    """
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = BlogComment.objects.filter(post=blogpost)
    new_comment = None
    comment_form = BlogCommentForm()

    # Code handling posting a comment, or rendering an error message if
    # the attempted post does not succeed
    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid():
            # Creating new comment object, not saving yet
            new_comment = comment_form.save(commit=False)
            # Assigning the comment to the current blogpost
            new_comment.post = blogpost
            new_comment.save()
            messages.success(request, 'Your comment has been added!')
            # Rendering an empty comment form after comment is posted
            comment_form = BlogCommentForm()
        else:
            comment_form = BlogCommentForm()
            messages.error(request, 'Something went wrong, your comment\
                                     was not added. Please try again.')

    context = {
        'blogpost': blogpost,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_details.html', context)


@login_required
def add_blogpost(request):
    """
    A view to add a blogpost
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    # Handling functionality of add a blog to the db, or returning an
    # error message if add blog did not succeed
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Successfully added blogpost!')
            return redirect(reverse('blog_details', args=[blogpost.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The blogpost was not added to the store')
    # Rendering an empty add blog form
    else:
        form = BlogpostForm()

    template = 'blog/add_blogpost.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_blogpost(request, blogpost_id):
    """
    A view to edit a blogpost
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    # Handling functionality of edit a blog to the db, or returning an
    # error message if edit blog did not succeed
    if request.method == 'POST':
        form = BlogpostForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Successfully updated blogpost!')
            return redirect(reverse('blog_details', args=[blogpost.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The blogpost was not updated.')

    # Rendering an edit form for the specific blog and message
    # to the user about which blogpost they are editing
    else:
        form = BlogpostForm(instance=blogpost)
        messages.info(request, f'You are editing "{blogpost.title}"')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def confirm_delete_blogpost(request, blogpost_id):
    """
    A view for rendering a template where deletion is confirmed or cancelled
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    # Getting the specific blog from the db
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    context = {
        'blogpost': blogpost,
    }

    template = 'blog/confirm_delete_blog.html'

    return render(request, template, context)


@login_required
def delete_blogpost(request, blogpost_id):
    """
    Delete a blogpost
    """
    # Stopping a user from accessing this functionality if
    # they are not logged in with superuser credentials
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    # Getting the specific blog and deleting it from the db
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogpost.delete()
    messages.success(request, 'Blogpost successfully deleted.')
    return redirect(reverse('blog'))
