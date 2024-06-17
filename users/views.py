from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import CustomUserLoginForm, CustomUserRegistrationForm

def custom_user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Chuyển hướng đến trang home sau khi đăng nhập thành công
    else:
        form = CustomUserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def custom_user_register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Chuyển hướng đến trang home sau khi đăng ký thành công
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def custom_user_logout(request):
    # Đảm bảo người dùng đã đăng nhập trước khi logout
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')  # Chuyển hướng đến trang home sau khi logout
    else:
        # Xử lý trường hợp người dùng chưa đăng nhập
        pass  # Điều hướng tới trang khác hoặc hiển thị thông báo lỗi tùy theo yêu cầu
