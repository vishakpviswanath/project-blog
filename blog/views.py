from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, EditProfile
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def first_page(request):
      return render(request, 'blog/first_page.html')

@login_required
def profile(request):
      args = {'user': request.user, 'title' : Post.objects.filter( author=request.user)}
      return render(request, 'blog/profile.html', args)


def author_profile(request , pk=None):
      if pk:
            user= User.objects.get(pk=pk)
      else:
            user= request.user
      args={'user': user}           
      return render(request, 'blog/author_profile.html', args)


@login_required
def profile_edit(request):
      if request.method=="POST":
            form= EditProfile( request.POST, instance=request.user)

            if form.is_valid():
                  form.save()
                  return redirect('author_profile')

      else:
            form = EditProfile(instance=request.user)
            args = {'form': form}
            return render(request, 'blog/profile_edit.html', args)
            

@login_required
def change_password(request):
      if request.method=="POST":
            form= PasswordChangeForm( data= request.POST, user=request.user)

            if form.is_valid():
                  form.save()
                  update_session_auth_hash(request, form.user)
                  return redirect('author_profile')

            else:
                  return redirect('change_password')

      else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'blog/change_password.html', args)



def post_list(request):
      user= User.objects.all()
      posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   
      args=  {'posts': posts, 'users': user}
      return render(request, 'blog/post_list.html', args)


def post_detail(request, pk):
      post=get_object_or_404(Post, pk=pk)
      return render(request, 'blog/post_detail.html', {'post': post})


@login_required
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


@login_required
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

