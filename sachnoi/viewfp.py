import random
import string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user  # Lấy thông tin người dùng hiện tại

        # Kiểm tra mật khẩu cũ có đúng không
        if not check_password(old_password, user.password):
            messages.error(request, "Mật khẩu cũ không đúng!")
            return redirect("change_password")

        # Kiểm tra mật khẩu mới và xác nhận có khớp không
        if new_password != confirm_password:
            messages.error(request, "Mật khẩu mới và xác nhận không khớp!")
            return redirect("change_password")

        # Cập nhật mật khẩu mới
        user.set_password(new_password)
        user.save()

        messages.success(request, "Mật khẩu đã được đổi thành công!")
        return redirect("login")  # Chuyển hướng về trang đăng nhập

    return render(request, "app/change_password.html")


def generate_password(length=8):
    characters = string.ascii_letters + string.digits # Bao gồm chữ cái, số và ký tự đặc biệt
    return ''.join(random.choices(characters, k=length))  
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = get_user_model().objects.get(email=email)
            new_password = generate_password()  
            user.password = make_password(new_password)  
            user.save()  
            subject = "Mật khẩu mới của bạn"
            message = f"Đây là mật khẩu mới của bạn: {new_password}"
            from_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, from_email, [email])  

            messages.success(request, "Mật khẩu mới đã được gửi đến email của bạn!")
            return redirect('login')  

        except get_user_model().DoesNotExist:
            messages.error(request, "Email không tồn tại!")
    
    return render(request, 'app/forgot_password.html')

