from django.contrib import admin
from django import forms
from .models import Message

class MessageAdminForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'  # Chọn tất cả các trường

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'timestamp', 'content']
    list_filter = ['timestamp']
    search_fields = ['sender__username', 'receiver__username', 'content']
    date_hierarchy = 'timestamp'
admin.site.register(Message, MessageAdmin)
