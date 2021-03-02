from django.urls import path

from . import views

app_name = "appusers"
urlpatterns = [
     
     path("", views.index, name="index"),
     path("account/register", views.register, name="register"),
     path("account/logout", views.logout_view, name="logout"),
     path("account/user/login", views.login_user, name="login_user"),
     path("account/user/dashboard", views.dashboard, name="dashboard"),
]