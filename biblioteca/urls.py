from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    path('admin/', admin.site.urls)
]
