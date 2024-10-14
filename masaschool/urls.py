from django.contrib import admin
from django.urls import path, include
from education.views import login_view  # Uvezite login_view iz education aplikacije

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education/', include('education.urls')),
    path('', login_view, name='login'),  # Postavite login_view kao početnu stranicu
]
