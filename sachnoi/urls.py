
from django.urls import path
from . import views, viewfp
urlpatterns = [
    path('', views.index, name='index'),  # trang chu
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('discover.html', views.discover, name='discover'),  
    path('author.html', views.author, name='author'),  
    path('category.html', views.category, name='category'),  
    path('login.html',views.loginpage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    path('signup.html',views.signup, name='signup'),
    path('forgot-password/', viewfp.forgot_password, name='forgot_password'),
    path('search/', views.search_results, name='search_results'),
]