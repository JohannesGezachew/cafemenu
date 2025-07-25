"""cafemenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include  # <-- Add this line
from django.http import HttpResponse
from django.http import JsonResponse
from cloudinary import uploader


def favicon_view(request):
    return HttpResponse(status=204) 

urlpatterns = [
    path('favicon.ico', favicon_view), 
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def test_upload(request):
    try:
        result = uploader.upload(
            "https://res.cloudinary.com/demo/image/upload/sample.jpg",
            folder="render_test"
        )
        return JsonResponse({"status": "success", "url": result['secure_url']})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)