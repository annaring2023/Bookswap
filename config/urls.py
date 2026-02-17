from django.contrib import admin
from django.urls import path
from users.views import login_view
from config.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
]
