from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from education.views import login_view  # Uvezite login_view iz education aplikacije

urlpatterns = [
    path('admin/', admin.site.urls),
    path('education/', include('education.urls')),
    path('', RedirectView.as_view(url='education/')),  # Preusmjeri na education/
    path('accounts/login/', login_view, name='login'),  # Preusmjeri na vlastitu login funkciju
]
