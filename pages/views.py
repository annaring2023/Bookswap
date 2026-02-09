from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    # Дані, які ми хочемо передати на сторінку (текст, списки тощо)
    context = {
        "title": "Мій перший макет",
        "welcome_message": "Привіт! Це текст з Django view.",
        "button_text": "Натисни мене",
        "items": ["Елемент 1", "Елемент 2", "Елемент 3"]
    }
    return render(request, 'home.html', context)
