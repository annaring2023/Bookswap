from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_user, name='register'), # Адреса для реєстрації
    path('login/', views.login_user, name='login_user'),     # Адреса для входу
]
