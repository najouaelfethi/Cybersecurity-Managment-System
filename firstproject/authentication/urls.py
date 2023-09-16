from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage, name="home-page"),
    path('register/', views.Register, name="register-page"),
    path('login/', views.Login, name="login-page"),
    path('logout/', views.logoutuser, name='logout'),
    path('test/', views.test, name='test'),
    path("landing", views.landinpage, name = "landing"),
    path("login_DNSSI/", views.login_DNSSI, name = "login_DNSSI"),
    path("dropmenu/", views.dropmenu, name = "dropmenu"),

]
