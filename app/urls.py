from django.contrib import admin
from django.urls import path, include
from electronic import apiView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronic/', include('electronic.urls')),


]
