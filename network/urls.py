
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:comment>", views.comment, name="comment"),
    path("user_profile", views.user_profile, name="user_profile"),
    path("info", views.info, name="info"),
    path("likes", views.liking, name="likes"),
    path("following", views.following, name="following"),
    path("profile", views.profile, name="profile"),
    path("run", views.run, name="run"),
    path("edit", views.edit, name="edit"),
]
