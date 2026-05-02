from django.contrib import admin
from django.utils.text import Truncator
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, CommentLike, Category

class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for Post
    Uses Summernote rich text editor for content field
    """
    list_display = ('title', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status', 'post_type', 'created_on')
    exclude = ['excerpt',]
    filter_horizontal = ['categories',]
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Comment
    Uses Truncator to produce a short preview for the admin list view
    """
    list_display = ('comment_preview', 'created_on')
    search_fields = ('content',)

    def comment_preview(self, obj):
        preview = Truncator(obj.content)
        return preview.chars(50)
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'label_colour')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLike)
admin.site.register(Category, CategoryAdmin)
