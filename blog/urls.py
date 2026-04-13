from django.urls import path
from . import views

urlpatterns = [
    path('digging_deeper/', views.PostList.as_view(), name='digging_deeper'),
    path('', views.home_page, name='home'),
    path('<slug:slug>/', views.read_post, name='read_post'),
]