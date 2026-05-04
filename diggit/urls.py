"""
URL configuration for diggit project.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls'), name='contact-urls'),
    path('summernote', include('django_summernote.urls')),
    path('', include("blog.urls"), name='blog-urls'),
]
