# chat/forms.py

from django import forms
from .models import Message

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
class AdminMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content']