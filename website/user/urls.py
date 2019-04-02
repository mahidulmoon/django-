from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.main_page,name='welcome_page'),
    path('/register/', views.register,name='register'),
    path('/login/', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),

]