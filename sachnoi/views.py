from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponse , JsonResponse
from gtts import gTTS # type: ignore
from sachnoi.models import  Books
from .forms import TextToSpeechForm
from io import BytesIO
from . models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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


def create_text_entry(request):
    # Lưu văn bản vào database
    entry = TextEntry( content="Chào mừng bạn đến với thế giới lập trình Python. Đây là một ví dụ để kiểm tra tính năng chuyển văn bản thành giọng nói bằng gTTS. Chúc bạn thành công!")
    entry.save()
    
    return HttpResponse("Đã lưu văn bản thành công!")

def home(request):
    entries = TextEntry.objects.all()
    return render(request,'app/index.html',{'entries': entries})
def author(request):
    return render(request,'app/author.html')
def category(request):
    return render(
        request,'app/category.html'
    )
def discover(request):
    return render(request,'app/discover.html')
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

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
def convert_text_to_speech(request, text_id):
    from django.shortcuts import get_object_or_404  
    entry = get_object_or_404(TextEntry, id=text_id)
    tts = gTTS(text=entry.content, lang='vi')
    response = HttpResponse(content_type='audio/mpeg')
    tts.write_to_fp(response)
    response['Content-Disposition'] = f'attachment; filename="{entry.title}.mp3"'
    return response

def testapi(request):
    data = list(Books.objects.values())
    return JsonResponse(data ,safe=False)
def book_list(request):
    """
    View để hiển thị danh sách tất cả các sách.
    """
    books = Books.objects.all()  # Lấy tất cả sách từ cơ sở dữ liệu
    return render(request, 'app/book_list.html', {'books': books})

def book_detail(request, pk):
    """
    View để hiển thị chi tiết một cuốn sách.
    """
    book = get_object_or_404(Books, pk=pk)  # Lấy sách theo id (pk)
    return render(request, 'app/book_detail.html', {'book': book})