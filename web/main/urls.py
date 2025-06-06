"""main URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('epaper/', include(('epaper.urls', 'epaper'), namespace='epaper')),
    path('customers/', include(('customers.urls', 'customers'), namespace='customers')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 新增 media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)