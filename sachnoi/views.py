from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse , JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from sachnoi.models import  Books , Authors
from .forms import TextToSpeechForm
from io import BytesIO
from . models import *
import json
from django.contrib.auth.forms import UserCreationForm


# View page 
def index(request):
    """
    View để hiển thị danh sách tất cả các sách.
    """
    books = Books.objects.all()  # Lấy tất cả sách từ cơ sở dữ liệu
    return render(request, 'app/index.html', {'books': books})
def book_detail(request, pk):
    """
    View để hiển thị chi tiết một cuốn sách.
    """
    book = get_object_or_404(Books, pk=pk)  # Lấy sách theo id (pk)
    return render(request, 'app/book_detail.html', {'book': book})
def author(request):
    author = Authors.objects.all().distinct()
    return render(request,'app/author.html',{'author':author})
def category(request):
    books1 = Books.objects.all().filter(category_id=1)
    books2 = Books.objects.all().filter(category_id=2)
    books3 = Books.objects.all().filter(category_id=3)
    books4 = Books.objects.all().filter(category_id=4)
    books5 = Books.objects.all().filter(category_id=5)
    books6 = Books.objects.all().filter(category_id=6)

    return render(
        request,'app/category.html', {'books1': books1 , 'books2': books2 , 'books3': books3 , 'books4': books4 , 'books5': books5 , 'books6': books6}
    )
def discover(request):
    return render(request,'app/discover.html')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')  # Nếu người dùng đã đăng nhập, chuyển hướng đến trang chủ.
    if request.method == "POST":
        name = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=name, password=pass1)
        if user is not None:
            login(request, user)  # Đăng nhập người dùng.
            return redirect('home')  # Chuyển hướng đến trang chủ.
        else: messages.info(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')

    context = {}
    return render(request, 'app/login.html', context)
def logoutPage(request):
    logout(request)  # Đăng xuất người dùng.
    return redirect('login')  # Chuyển hướng đến trang đăng nhập.

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request,'app/signup.html', context)

def forgot_password(request):
    return render(request,'app/forgot_password.html')

def enter_OTP_code(request):
    return render(request,'app/enter_OTP_code.html')


