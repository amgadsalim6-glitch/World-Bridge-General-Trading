from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    # 🌍 ضبط اللغة (أول مرة بس)
    if 'django_language' not in request.session:
        request.session['django_language'] = 'en'

    services = [
        {"title": "Import & Export", "description": "Global trade", "icon": "fas fa-ship"},
        {"title": "Shipping", "description": "Fast delivery", "icon": "fas fa-truck"},
        {"title": "Real Estate", "description": "Investment", "icon": "fas fa-building"},
        {"title": "Agencies", "description": "Partnerships", "icon": "fas fa-handshake"},
    ]

    # 📸 قراءة صور السلايدر
    slider_path = os.path.join(settings.STATICFILES_DIRS[0], 'slider')

    images = []
    if os.path.exists(slider_path):
        for file in os.listdir(slider_path):
            if file.endswith(('.jpg', '.png', '.jpeg')):
                images.append('slider/' + file)

    # 🔢 ترتيب الصور 1,2,3...
    try:
        images.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    except:
        pass  # لو اسم صورة مش رقم

    return render(request, "core/home.html", {
        "services": services,
        "images": images
    })


def services(request):
    return render(request, "core/services.html")


def contact(request):
    return render(request, "core/contact.html")


def about(request):
    return render(request, 'core/about.html')