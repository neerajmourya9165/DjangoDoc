from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    myposts=Post.objects.filter(author=request.user)
    template=loader.get_template('posts.html')
    context={
        'myposts':myposts,
    }
    return HttpResponse(template.render(context,request))



@login_required(login_url='login')
def add(request):
    template=loader.get_template('addpost.html')
    return HttpResponse(template.render({},request))

@login_required(login_url='login')
def addrecord(request):
    x=request.POST['title']
    y=request.POST['body']
    post=Post(title=x,body=y,author=request.user)
    post.save()
    return HttpResponseRedirect(reverse('index'))



@login_required(login_url='login')
def delete(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))



@login_required(login_url='login')
def update(request,id):
    post=Post.objects.get(id=id)
    template=loader.get_template('updatepost.html')
    context={
        'post':post,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def updaterecord(request,id):
    title=request.POST['title']
    body=request.POST['body']
    post_obj=Post.objects.get(id=id)
    post_obj.title=title
    post_obj.body=body
    post_obj.save()
    return HttpResponseRedirect(reverse('index'))

def registerPage(request):
    form=UserCreationForm()

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return HttpResponseRedirect(reverse('login'))

    template=loader.get_template('register.html')
    context={'form':form}
    return HttpResponse(template.render(context,request))

def loginPage(request):
    template = loader.get_template('login.html')
    context = {}

    if request.method=="POST":
        username=request.POST.get('username')

        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.info(request,'Username or Password incorrect')
            return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context,request))

def logoutUser(request):
    logout(request)
    return redirect('login')


# def search(request):
#     query=request.GET['search']
#     all_post=Post.objects.filter(title_contains=query)
#     params={
#         'all_post':all_post
#     }
#     return render(request,'search.html',params)