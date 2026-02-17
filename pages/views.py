from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    context = {
        "title": "Мій перший макет",
        "welcome_message": "Привіт! Це текст з Django view.",
        "button_text": "Натисни мене",
        "items": ["Елемент 1", "Елемент 2", "Елемент 3"]
    }
    return render(request, 'home.html', context)
def profile_view(request):
    return render(request, 'profile.html')
