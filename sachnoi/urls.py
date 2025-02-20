
from django.urls import path
from . import views, viewfp
urlpatterns = [
    path('', views.index, name='index'),  # trang chu
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('discover/', views.discover, name='discover'),  
    path('author/', views.author, name='author'),  
    path('category/', views.category, name='category'),  
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('favorite/',views.favorite, name='favorite'),
    path('favorite_books/',views.favorite_books, name='favorite_books'),
    path('profile/',views.profile, name='profile'),
    path('save_book/',views.save_book, name='save_book'),
    path('account/', views.account, name='account'),
    path('book_history/',views.book_history, name='book_history'),
    path('forgot-password/', viewfp.forgot_password, name='forgot_password'),
    path('search/', views.search_results, name='search_results'),
    path("change-password/", viewfp.change_password, name="change_password"),
    path('text_to_speech/', views.text_to_speech_view, name='text_to_speech'),
    path('author_detail/', views.author_detail, name='author_detail'),
    path('trending_page/', views.trending_page, name='trending_page'),
    path('toggle_favorite/<int:book_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('download_book/<int:book_id>/', views.download_book, name='download_book'),
]