from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Головна сторінка
def home(request):
    return render(request, 'home.html')

# Сторінка профілю (пускає тільки тих, хто увійшов)
def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')  # Якщо не зайшов - викидаємо на головну
    return render(request, 'profile.html')

# Логіка реєстрації
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Перевірка, чи існує такий юзер
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Таке ім\'я вже зайняте!')
            return redirect('home')

        # Створення користувача
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user) # Одразу входимо
        return redirect('profile')

    return redirect('home')

# Логіка входу
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username'] # Тут беремо дані з форми
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Невірний логін або пароль')
            return redirect('home')

    return redirect('home')
