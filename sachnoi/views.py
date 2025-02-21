from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse , JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gtts import gTTS
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from sachnoi.models import  Books , Authors
from .forms import TextToSpeechForm
from django.db.models import Q, Count
from io import BytesIO
from . models import *
import json
from django.contrib.auth.forms import UserCreationForm
from .chatbot_main import ask_bloom

# View page 


def index(request):
    """
    View hiển thị danh sách sách thịnh hành và sách mới nhất.
    """
    books = Books.objects.all()  # Lấy tất cả sách
    today = datetime.now().date()

    # Lấy sách thịnh hành theo ngày
    trending_today = Trending.objects.filter(date=today).order_by('-views')[:5]

    return render(request, 'app/index.html', {
        'books': books,
        'trending_today': trending_today,
    })
def book_detail(request, pk):
    """
    View để hiển thị chi tiết một cuốn sách và xử lý input người dùng bằng AJAX.
    """
    b = Books.objects.all()
    book = get_object_or_404(Books, pk=pk)

    today = datetime.now().date()
    trending_entry, created = Trending.objects.get_or_create(book=book, date=today)
    trending_entry.views += 1
    trending_entry.save()

    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Kiểm tra header X-Requested-With để xác định yêu cầu AJAX
        user_message = request.POST.get('user_message', '')
        if user_message:
            response = ask_bloom(book.text_content, user_message)
            print("Bot Response:", response)
            return JsonResponse({'response': response})  # Trả về JSON

    # Trả về trang HTML bình thường nếu là yêu cầu GET
    return render(request, 'app/detail.html', {'book': book, 'b': b})
def author(request):
    author = Authors.objects.all().distinct()
    return render(request,'app/author.html',{'author':author})
def author_detail(request, id):
    author = get_object_or_404(Authors, id=id)
    # author = Authors.objects.get(id=id)
    book = Books.objects.filter(author=author)  # Lấy tất cả sách của tác giả này
    return render(request, 'app/author_detail.html', {'author': author , 'book':book})
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
# def author_detail(request):
#     return render(request,'app/author_detail.html')
def trending_page(request):
    return render(request,'app/trending_page.html')
# view login | signup



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')  # Nếu đã đăng nhập, chuyển hướng về trang chủ

    if request.method == "POST":
        name = request.POST.get('username')
        pass1 = request.POST.get('password')

        if not name or not pass1:
            messages.warning(request, 'Vui lòng nhập đầy đủ thông tin!')
            return redirect('login')

        user = authenticate(request, username=name, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, '🎉 Đăng nhập thành công! Chào mừng bạn trở lại.')

            return redirect('index')  # Chuyển đến index nhưng thông báo vẫn còn
        else:
            messages.error(request, '❌ Tên đăng nhập hoặc mật khẩu không đúng!')
            return redirect('login')
    
    return render(request, 'app/login.html')


def logoutPage(request):
    logout(request)  # Đăng xuất người dùng.
    return redirect('login')  # Chuyển hướng đến trang đăng nhập.



def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đăng ký thành công! Bạn sẽ được chuyển hướng đến trang đăng nhập sau vài giây')
            return render(request, 'app/signup.html', {'form': CreateUserForm(), 'redirect': True})  
        else:
            messages.error(request, "Đăng ký thất bại. Vui lòng kiểm tra lại thông tin.") 
            # form = CreateUserForm()  
    else:
        form = CreateUserForm()

    return render(request, 'app/signup.html', {'form': form})

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
def trending_page(request):
    today = datetime.now().date()

    # Lấy danh sách sách thịnh hành hôm nay
    trending_today = Trending.objects.filter(date=today).order_by('-views')[:10]

    # Lấy sách thịnh hành theo tuần
    week_start = today - timedelta(days=7)
    trending_week_raw = Trending.objects.filter(date__range=[week_start, today]).order_by('-views')
    trending_week = []
    seen_books = set()
    for trend in trending_week_raw:
        if trend.book.id not in seen_books:
            trending_week.append(trend)
            seen_books.add(trend.book.id)
        if len(trending_week) >= 10:  # Giới hạn số lượng sách hiển thị
            break

    # Lấy sách thịnh hành theo tháng
    month_start = today.replace(day=1)
    trending_month_raw = Trending.objects.filter(date__range=[month_start, today]).order_by('-views')
    trending_month = []
    seen_books = set()
    for trend in trending_month_raw:
        if trend.book.id not in seen_books:
            trending_month.append(trend)
            seen_books.add(trend.book.id)
        if len(trending_month) >= 10:  # Giới hạn số lượng sách hiển thị
            break

    return render(request, 'app/trending_page.html', {
        'trending_today': trending_today,
        'trending_week': trending_week,
        'trending_month': trending_month,
    })
