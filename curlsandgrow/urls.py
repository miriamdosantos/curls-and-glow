# curlsandgrow/urls.py

from django.conf.urls import handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('booking/', include('apps.booking.urls')),
    path("contact/", include('apps.contact.urls')),
    path('', include('apps.services.urls')),
]

