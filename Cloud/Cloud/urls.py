"""
URL configuration for Cloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.http import HttpResponseRedirect


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('chat.urls')),  # <--- Dòng này rất quan trọng!
    # Tuỳ chọn: root path trả về welcome message
    # path('', lambda request: JsonResponse({'message': 'Welcome to the Chat API'})),
    path('', lambda request: HttpResponseRedirect('/api/')),
]