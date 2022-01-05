from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('plantillas.urls')),
    path('plantillas/', include('plantillas.urls')),
    path('admin/', admin.site.urls),
]
