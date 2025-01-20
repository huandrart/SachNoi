from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),  # URL để hiển thị danh sách sách
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    # path('', views.home, name='home'),  
    path('index.html', views.home, name='home'),  
    path('discover.html', views.discover, name='discover'),  
    path('author.html', views.author, name='author'),  
    path('category.html', views.category, name='category'),  
    path('login.html',views.loginpage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    path('signup.html',views.signup, name='signup'),
    path('forgot-password.html', views.forgot_password, name='forgot_password'),
    path('enter_OTP_code.html', views.enter_OTP_code, name='enter_OTP_code'),
    path('convert/<int:text_id>/', views.convert_text_to_speech, name='convert_text_to_speech'),
    path('create-entry/', views.create_text_entry, name='create_entry'),
    path('testapi/',views.testapi , name='testapi'),
    path('text_to_speech.html', views.text_to_speech_view, name='text_to_speech'),

]