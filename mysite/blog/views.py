
from django.urls import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .forms import ContactForm
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView

from .forms import CommentForm
from django.views import View
# Create your views here.


           
def index(request):
   
   form = ContactForm(request.POST or None)
   latest_posts= Post.objects.all().order_by('-created_on')[:3]
   return render(request, "blog/index.html",{
      "posts": latest_posts,
      "form": form
   })

class PostsView(ListView):
   model = Post
   template_name = "blog/posts.html"
   ordering = ["-created_on"]
   context_object_name = "all_posts"
   

class PostDetailView(View):
      def get(self,request,slug):
              post = Post.objects.get(slug=slug)
              context = {
                 "post": post,
                 "comment_form": CommentForm(),
                 "comments": post.comments.all().order_by("-created_on")
              }
              return render(request,"blog/post.html",context)
      def post(self,request,slug):
              post = Post.objects.get(slug=slug)
              comment_form = CommentForm(request.POST)
              username = request.user
              if comment_form.is_valid():
                     comment = comment_form.save(commit=False)
                     comment.post = post
                     comment.user_name = username
                     comment.save()
                     return HttpResponseRedirect(reverse("single_post",args=[slug]))
              else:
                     context = {
                        "post": post,
                        "comment_form": comment_form,
                        "comments": post.comments.all().order_by("-created_on")
                     }
                     return render(request,"blog/post.html",context)     
                
         
        
                     
def handleSignup(request):
       if request.method == "POST":
              username = request.POST["username"]
              email = request.POST["email"]
              password = request.POST["password"]
              confirm_password = request.POST["confirm-password"]
              
              #checks and validations
              if len(username) > 10 or len(username) < 3:
                     messages.error(request,"Username must be between 3 and 10 characters")
                     return HttpResponseRedirect(reverse("index"))
              if not username.isalnum():
                      messages.error(request,"Username must be alphanumeric")
                      return HttpResponseRedirect(reverse("index"))
              if password != confirm_password:
                     messages.error(request,"Passwords do not match")
                     return HttpResponseRedirect(reverse("index"))
              if User.objects.filter(username = username):
                     messages.error(request, "This username is already taken")
                     return HttpResponseRedirect(reverse("index"))
              if User.objects.filter(email = email):
                     messages.error(request, "This email aready exists")
                     return HttpResponseRedirect(reverse("index"))
              myuser = User.objects.create_user(username,email,password)
              myuser.save()
              messages.success(request,"You have successfully signed up")
              return HttpResponseRedirect(reverse("index"))
       
       else:
              messages.error(request,"Invalid Request")
              return HttpResponseRedirect(reverse("index"))

def handleLogin(request):
       if request.method == "POST":
              username = request.POST["login-username"]
              password = request.POST["login-password"]
              
              user = authenticate(username=username,password=password)
              
              if user is not None:
                     login(request,user)
                     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
              else:
                     messages.error(request,"Invalid Credentials")
                     return HttpResponseRedirect(reverse("index"))
         
       else:
              messages.error(request,"Invalid Request")
              return HttpResponseRedirect(reverse("index"))

def handleLogout(request):
   logout(request)
   messages.success(request,"You have successfully logged out")
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))