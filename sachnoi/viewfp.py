import random
import string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# Gửi mã OTP
def send_otp(email):
    otp = ''.join(random.choices(string.digits, k=6))  # Tạo mã OTP 6 chữ số
    subject = "Mã OTP để khôi phục mật khẩu"
    message = f"Mã OTP của bạn là: {otp}"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [email])  # Gửi email chứa mã OTP
    return otp

# Quên mật khẩu - Nhận email từ người dùng
def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # Kiểm tra email có tồn tại trong hệ thống không
        try:
            user = get_user_model().objects.get(email=email)
            otp = send_otp(email)
            request.session['otp'] = otp  # Lưu OTP vào session để so sánh sau
            request.session['email'] = email  # Lưu email vào session
            return redirect('enter_otp_code')
        except get_user_model().DoesNotExist:
            messages.error(request, "Email không tồn tại!")
    
    return render(request, 'app/forgot_password.html')

# Nhập mã OTP
def enter_OTP_code(request):
    if request.method == "POST":
        otp_input = request.POST.get('otp')
        if otp_input == request.session.get('otp'):  # So sánh OTP nhập vào với OTP trong session
            return redirect('reset_password')  # Chuyển tới trang thay đổi mật khẩu
        else:
            messages.error(request, "Mã OTP không chính xác!")
    
    return render(request, 'app/enter_OTP_code.html')

# Đặt lại mật khẩu
def reset_password(request):
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password:
            email = request.session.get('email')
            user = get_user_model().objects.get(email=email)
            user.password = make_password(new_password)  # Mã hóa mật khẩu
            user.save()  # Lưu mật khẩu mới vào DB
            messages.success(request, "Mật khẩu đã được thay đổi thành công!")
            return redirect('login')  # Chuyển hướng về trang đăng nhập
        else:
            messages.error(request, "Mật khẩu xác nhận không khớp!")
    
    return render(request, 'app/reset_password.html')
