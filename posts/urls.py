from django.urls import path
from . import views

urlpatterns = [
    path('posts/new/', views.new_post, name = 'new post'),
    path('posts/leave_a_comment/', views.leave_a_comment, name = 'leave a comment'),
    
    # main page of site!
    path('', views.index, name = 'index'),
]