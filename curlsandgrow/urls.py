# curlsandgrow/urls.py

from django.conf.urls import handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include
from apps.services.views import custom_403_view,custom_404_view,custom_500_view

handler403 = custom_403_view
handler404 = custom_404_view
handler500 = custom_500_view
urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('booking/', include('apps.booking.urls')),
    path("contact/", include('apps.contact.urls')),
    path('', include('apps.services.urls')),
    
]
