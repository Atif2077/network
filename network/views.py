from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import User, Post, Statistics_user, Post_comments


def index(request):
    posts = Post.objects.all().order_by("-time")
    page_num = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)


    try:
        post = paginator.page(page_num)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)    
    if request.method == "POST":
        comment= request.POST["post"]
        user = request.user
        username = user.username
        if username == "":
            return HttpResponseRedirect("/login")
        Post.objects.create(post=comment, user=username)
        
        return HttpResponseRedirect(reverse("index"))
    return render(request, "network/index.html", {
        "posts": post,
        "comment": 1,
        "profile": "user"
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            Statistics_user.objects.create(user=username)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url='/login')    
def info(request):
    if request.method == "POST":
        try:
            global post_id
            post_id = request.POST["id"]
        except MultiValueDictKeyError:
            post_id = False
        return HttpResponseRedirect(reverse("comment", kwargs={'comment':post_id}))

@login_required(login_url='/login')
def comment(request, comment):
    if request.method == "POST":
        users = request.user
        name = users.username
        comment = request.POST["comment"]
        Post_comments.objects.create(user=name, comments=comment, comment_id=post_id)
        data = Post.objects.get(post_id=post_id)
        data.comments += 1
        data.save()
        return HttpResponseRedirect(reverse("comment", kwargs={'comment':post_id}))
    
    comments = Post_comments.objects.filter(comment_id=post_id).order_by("-time")
    posts = Post.objects.filter(post_id=post_id)
    return render(request, "network/comment.html", {
        "posts": posts,
        "comments": comments,
        "comment": 1
        
    })      
    

@login_required(login_url='/login')   
def user_profile(request):
    if request.method == "POST":
        users = request.user
        name = users.username
        bio = request.POST.get("bio")
        profile_img = request.POST.get("profile_img")
        change = Statistics_user.objects.get(user=name)
        change.bio = bio
        change.profile_img = profile_img
        change.save()
        return HttpResponseRedirect(reverse("user_profile"))
    
    
    users = request.user
    name = users.username
    post = Post.objects.filter(user=name).order_by("-time")
    info = Statistics_user.objects.filter(user=name)
    u = Statistics_user.objects.get(user=name)
    nam = u.following.all()   
    return render (request, "network/user_profile.html",{
        "info": info,
        "posts": post,
        "wow": nam
    })

@login_required(login_url='/login')        
def liking(request):
    if request.method == "POST":
        post = Post.objects.get(post_id=post_id)
        users = request.user
        name = users.username
        user = User.objects.get(username=name)
        if user in post.liking.all():
            post.liking.remove(user)
            post.likes_no = post.likes_no - 1
            post.save()
        else:
            post.likes_no += 1
            post.liking.add(user)
            post.save()
        return HttpResponseRedirect(reverse("comment", kwargs={'comment':post_id}))
    

@login_required(login_url='/login')   
def following(request):
    users = request.user
    name = users.username
    follow = Statistics_user.objects.get(user=name)
    person = follow.following.all()
    posts = Post.objects.filter(user__in=follow.following.all().values("username")).order_by("-time")
    page_num = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)


    try:
        post = paginator.page(page_num)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    
    return render (request, "network/following.html", {
        "posts": post,
        "follow": person
    })

@login_required(login_url='/login')
def profile(request):
    if request.method == "POST":
        global post_name
        post_name = request.POST["post_name"]
        return HttpResponseRedirect(reverse("profile"))
    
    users = request.user
    user = users.username
    response = "following"
    u = Statistics_user.objects.get(user=user)
    t = User.objects.get(username=post_name)
    post = Post.objects.filter(user=post_name).order_by("-time")
    if t in u.following.all():
        response = "Unfollow"
    else:
        response = "follow"
    info = Statistics_user.objects.filter(user=post_name)
    n = Statistics_user.objects.get(user=post_name)
    nam = n.following.all()   
    return render (request, "network/profile.html",{
        "info": info,
        "profile": post_name,
        "response": response,
        "posts": post,
        "wow": nam
    })

@login_required(login_url='/login')   
def run(request):
    if request.method == "POST":
        users = request.user
        user = users.username
        u = Statistics_user.objects.get(user=user)
        t = User.objects.get(username=post_name)
        if user == post_name:
            return HttpResponseRedirect(reverse("user_profile"))
        elif t in u.following.all():
            u.following.remove(t)
        else:
            u.following.add(t)
        return HttpResponseRedirect(reverse("profile"))
    
@login_required(login_url='/login')
def edit(request):
    if request.method == "POST":
        post_id = request.POST.get("id")
        edit = request.POST.get("edit")
        p = Post.objects.get(post_id=post_id)
        p.post = edit
        p.save()
        return HttpResponseRedirect(reverse("user_profile"))

### Thank you very much ###
"""
    This is my project 4 for network

"""