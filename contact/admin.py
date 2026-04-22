from django.contrib import admin
from django.utils.text import Truncator
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_preview', 'created_on', 'read')
    search_fields = ('name', 'message')
    list_filter = ('read',)

    def message_preview(self, obj):
        preview = Truncator(obj.message)
        return preview.chars(50)

# Register your models here.
admin.site.register(Message, MessageAdmin)