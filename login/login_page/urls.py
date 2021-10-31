from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[

    path("", views.registerform, name="register"),
    path("login", auth_views.LoginView.as_view(template_name="login_page/login_page.html"), name='login'),
    path("logout", auth_views.LogoutView.as_view(template_name="login_page/logout_page.html"), name='logout'),
    path("feed",views.account,name="blog-feed"),
    path("details", views.details, name="details"),
]