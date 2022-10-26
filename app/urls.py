from django.contrib import admin
from django.urls import path, include
from electronic import apiView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronic/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='electronic'))

]
