
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),  # trang chu
    # path('admin/', admin.site.urls),
    # path('', views.index, name='home'),  
    # path('index.html', views.index, name='index'),  
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('discover.html', views.discover, name='discover'),  
    path('author.html', views.author, name='author'),  
    path('category.html', views.category, name='category'),  
    path('login.html',views.loginpage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    path('signup.html',views.signup, name='signup'),
    path('forgot-password.html', views.forgot_password, name='forgot_password'),
    path('enter_OTP_code.html', views.enter_OTP_code, name='enter_OTP_code'),


]