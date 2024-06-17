# chat/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message
from .forms import UserMessageForm, AdminMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def chat_home(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('chat:chat_home')
    else:
        form = UserMessageForm()

    messages_sent = Message.objects.filter(sender=request.user)
    messages_received = Message.objects.filter(receiver=request.user)
    all_messages = messages_sent | messages_received
    all_messages = all_messages.order_by('timestamp')

    context = {
        'form': form,
        'messages': all_messages,
    }
    return render(request, 'chat/index.html', context)
@login_required
def admin_send_message(request):
    if request.method == 'POST':
        form = AdminMessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('admin_send_message')
    else:
        form = AdminMessageForm()
    
    context = {
        'form': form,
    }
    return render(request, 'chat/admin_send_message.html', context)
def admin_chat(request):
    # Lấy tất cả các tin nhắn, có thể sắp xếp theo thời gian gửi
    messages = Message.objects.all().order_by('timestamp')

    # Nếu admin gửi tin nhắn
    if request.method == 'POST':
        form = AdminMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Đặt admin là người gửi
            message.save()
            form = AdminMessageForm()  # Reset form sau khi gửi tin nhắn thành công
    else:
        form = AdminMessageForm()

    context = {
        'messages': messages,
        'form': form,
    }
    return render(request, 'chat/admin_chat.html', context)