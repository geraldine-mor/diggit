from django.contrib import admin
from django.utils.text import Truncator
from .models import Post, Comment, CommentLike

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status',)
    exclude = ['excerpt',]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_preview', 'created_on')
    search_fields = ('content',)

    def comment_preview(self, obj):
        preview = Truncator(obj.content)
        return preview.chars(50)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLike)
