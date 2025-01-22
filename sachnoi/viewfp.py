import random
import string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User

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
            user = User.objects.get(email=email)
            otp = send_otp(email)
            request.session['otp'] = otp  # Lưu OTP vào session để so sánh sau
            request.session['email'] = email  # Lưu email vào session
            return redirect('enter_otp_code')
        except User.DoesNotExist:
            messages.error(request, "Email không tồn tại!")
    
    return render(request, 'app/forgot_password.html')

# Nhập mã OTP
def enter_OTP_code(request):
    if request.method == "POST":
        otp_input = request.POST.get('otp')
        if otp_input == request.session.get('otp'):
            return redirect('reset_password')  # Chuyển tới trang thay đổi mật khẩu
        else:
            messages.error(request, "Mã OTP không chính xác!")
    
    return render(request, 'app/enter_OTP_code.html')
