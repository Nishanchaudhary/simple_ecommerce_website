from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base',base_view, name='base' ),
    path('',home, name='home'),
    path('shop/',shop, name='shop'),
    path("add-to-cart/",add_to_cart, name="add_to_cart"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)