from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('app.urls') ),
    path('auth/', include('authentication.urls')),    
]