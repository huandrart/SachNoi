from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse , JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from sachnoi.models import  Books , Authors
from .forms import TextToSpeechForm
from django.db.models import Q
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
    View để hiển thị chi tiết một cuốn sách và xử lý input người dùng bằng AJAX.
    """
    b = Books.objects.all()
    book = get_object_or_404(Books, pk=pk)

    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Kiểm tra header X-Requested-With để xác định yêu cầu AJAX
        user_message = request.POST.get('user_message', '')
        if user_message:
            response = vodka(book.text_content, user_message)
            print("Bot Response:", response)
            return JsonResponse({'response': response})  # Trả về JSON

    # Trả về trang HTML bình thường nếu là yêu cầu GET
    return render(request, 'app/detail.html', {'book': book, 'b': b})
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
def profile(request):
    return render(request,'app/account.html')
def favorite(request):
    return render(request,'app/favorite_books.html')
def save_book(request):
    return render(request,'app/save_book.html')
def book_history(request):
    return render(request,'app/book_history.html')
def favorite_books(request):
    return render(request,'app/favorite_books.html')
def account(request):
    return render(request,'app/account.html')

# view login | signup

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')  # Nếu người dùng đã đăng nhập, chuyển hướng đến trang chủ.
    if request.method == "POST":
        name = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=name, password=pass1)
        if user is not None:
            login(request, user)  # Đăng nhập người dùng.
            return redirect('index')  # Chuyển hướng đến trang chủ.
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
            messages.success(request, 'Đăng ký thành công!')  
            return redirect('index')  
    context = {'form' : form}
    return render(request,'app/signup.html', context)


def search_results(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Books.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__name__icontains=query)
        )
    return render(request, 'app/search_results.html', {'query': query, 'results': results})

def text_to_speech_view(request):
    if request.method == "POST":
        form = TextToSpeechForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            print("Văn bản người dùng nhập:", text)
            try:
                tts = gTTS(text, lang='vi')
                audio_file = BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)
                print("Tạo file âm thanh thành công")
                
                action = request.POST.get("action")  # Lấy hành động từ nút nhấn
                
                if action == "play":
                    # Trả file MP3 để phát trực tiếp
                    response = HttpResponse(audio_file, content_type="audio/mpeg")
                    response['Content-Disposition'] = 'inline; filename="output.mp3"'
                    return response
                elif action == "download":
                    # Trả file MP3 để tải về
                    response = HttpResponse(audio_file, content_type="audio/mpeg")
                    response['Content-Disposition'] = 'attachment; filename="output.mp3"'
                    return response
            except Exception as e:
                print("Lỗi khi chuyển văn bản thành giọng nói:", e)
                return render(request, 'app/text_to_speech.html', {
                    'form': form,
                    'error': f"Không thể chuyển văn bản thành giọng nói: {str(e)}"
                })
    else:
        form = TextToSpeechForm()
    return render(request, 'app/text_to_speech.html', {'form': form})
