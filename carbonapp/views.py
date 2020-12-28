from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import user_prof , post_image
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    cp=False
    posts=post_image.objects.order_by('-id')
    if request.user.is_authenticated:
        a=user_prof.objects.filter(user=request.user)
        if not a.exists():
            cp=True
   
    param={'cp':cp,'posts':posts}
    print(cp)
    return render(request,'home.html',param)

def comp_prof(request):
    if request.method=='POST':
        Img=request.FILES
        
        profile=Img.get('profile')
        bio=request.POST['bio']
        update=user_prof.objects.create(user=request.user,profile=profile,bio=bio)
        update.save()
        return redirect('/')
    return render(request,'comp_prof.html')


@login_required(login_url='/accounts/google/login/')
def postpic(request):
    if request.user.is_authenticated:
        a=user_prof.objects.filter(user=request.user)
        if not a.exists():
            return redirect('/completeprofile')
   
    if request.method=='POST':
        Img=request.FILES
        
        img=Img.get('img')
        caption=request.POST['caption']
        post=post_image.objects.create(user=request.user,img=img,caption=caption)
        post.save()
        return redirect('/')
    return render(request,'post_pic.html')