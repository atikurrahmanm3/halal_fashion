from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('aboutus',include('aboutus.urls')),
    path('product',include('product.urls')),
    path('blog',include('blog.urls')),
]
