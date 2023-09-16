from django.urls import path
from . import views
from chatgpt.views import answer

urlpatterns = [
    path("index", views.index, name="index"),
    path("/article/<slug:slug>", views.detail, name="detail"),
    path("/like_blog", views.like_blog, name = "like"),
    path("/add_comment", views.addComment, name = "add_comment"),
    path('chatgpt/answer/', answer, name='answer'),

    
]
