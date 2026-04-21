from django.urls import path
from . import views

urlpatterns = [
    path('digging_deeper/', views.PostList.as_view(), name='digging_deeper'),
    path('diggit_forum/', views.forum_list, name='diggit_forum'),
    path('', views.home_page, name='home'),
    path('<slug:slug>/', views.read_post, name='read_post'),
    path('<slug:slug>/edit_post/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete_post/', views.delete_post, name='delete_post'),
]