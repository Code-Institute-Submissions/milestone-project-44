from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def createpost(request, pk=None):
    """ A view that allows the logged in user to create a new blog post. """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)       
        if form.is_valid:
            post = form.save()
            allposts = Post.objects.all()
            context = {'allposts': allposts}
            return render(request, 'home.html', context)
    else:
        form = PostForm(instance=post)
        return render(request, 'create.html', {'form':form})
    
def home(request):
    """ A simple view to render all the blog posts submitted. """
    allposts = Post.objects.all()

    context = {'allposts': allposts}

    return render(request, 'home.html', context)

def detail_post_view(request, id=None):
    """ A view that allows the user to display the full length of the post. """
    eachpost = get_object_or_404(Post, id=id)
    context = {'eachpost': eachpost}
    return render(request, 'detail.html', context)

