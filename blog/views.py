from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def first_page(request):
      return render(request, 'blog/first_page.html')

def profile(request):
      args = {'user': request.user, 'title' : Post.objects.filter( author=request.user)}
      return render(request, 'blog/profile.html', args)

def post_list(request):
      posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   
      return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
      post=get_object_or_404(Post, pk=pk)
      return render(request, 'blog/post_detail.html', {'post': post})



def post_new(request):
      if request.method =="POST":
            form = PostForm(request.POST)
            if form.is_valid():
                  post = form.save(commit=False)
                  post.author = request.user
                  post.published_date = timezone.now()
                  post.save()
                  return redirect('post_detail', pk=post.pk)
      
      else:
            form = PostForm()
            return render(request,'blog/post_edit.html',{'form': form})      



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = str(request.user)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def register(request):
      if request.method =='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('post_list')

      else:
            form = UserCreationForm()

            args = {'form':form}
            return render(request, 'blog/reg_form.html', args)      

