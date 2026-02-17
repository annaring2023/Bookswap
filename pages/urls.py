from django.urls import path
from .views import home_page_view, profile_view  # <-- Ми додали сюди profile_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('profile/', profile_view, name='profile'), # <-- А сюди додали нову адресу
]
