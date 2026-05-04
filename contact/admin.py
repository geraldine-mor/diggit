from django.contrib import admin
from django.utils.text import Truncator
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for :model:`Message`
    Uses Truncator to produce a short preview for the admin list view
    """
    list_display = ('message_preview', 'created_on', 'read')
    search_fields = ('name', 'message')
    list_filter = ('read',)

    def message_preview(self, obj):
        preview = Truncator(obj.message)
        return preview.chars(50)


admin.site.register(Message, MessageAdmin)