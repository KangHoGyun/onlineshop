from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('coupon/', include('coupon.urls')),
    path('order/', include('order.urls')),
    path('', include('shop.urls'))
]
