from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('aboutus/',include('aboutus.urls')),
    path('product/',include('product.urls')),
    path('blog/',include('blog.urls')),
    path('shopping/',include('shopping.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
