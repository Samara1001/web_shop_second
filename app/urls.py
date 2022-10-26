from django.contrib import admin
from django.urls import path, include
from electronic import apiView



from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('electronic/', include('electronic.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='electronic'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

