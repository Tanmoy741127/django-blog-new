from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("posts",views.PostsView.as_view(),name="posts"),
    path("posts/<slug>",views.PostDetailView.as_view(),name="single_post"),
    path("signup",views.handleSignup,name="signup"),
    path("login",views.handleLogin,name="login"),
    path("logout",views.handleLogout,name="logout"),

]