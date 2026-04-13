from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status',)

# Register your models here.
admin.site.register(Post, PostAdmin)
