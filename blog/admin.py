from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status',)
    exclude = ['excerpt',]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
