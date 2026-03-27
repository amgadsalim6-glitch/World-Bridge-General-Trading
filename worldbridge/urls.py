from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 مهم لزرار تغيير اللغة
    path('i18n/', include('django.conf.urls.i18n')),
]

# 🔥 ده اللي بيخلي /ar/ و /en/ يشتغلوا
urlpatterns += i18n_patterns(
    path('', include('core.urls')),
)