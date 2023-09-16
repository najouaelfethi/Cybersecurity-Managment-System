from django.urls import path
from . import views

urlpatterns=[
    path('home', views.home, name='home'),
    path('answer', views.answer, name='answer'),

]