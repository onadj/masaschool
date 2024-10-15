from django.contrib import admin
from django.urls import path, include
from education.views import login_view, home_view  # Uvezite home_view iz education aplikacije

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education/', include('education.urls')),
    path('', login_view, name='login'),  # Postavite login_view kao početnu stranicu
    path('home/', home_view, name='home'),  # Početna stranica nakon prijave
]

