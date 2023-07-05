from Blog import views
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    #path('home/', views.home, name='home'),
    #path('signup/', views.register, name='signup'),
    #path('login/', views.login, name='login'),
    #path('home/', views.yes, name='yes'),
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='details'),
    path('blog/new', BlogCreateView.as_view(), name='blog_form'),

]