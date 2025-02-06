import random
import string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


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

