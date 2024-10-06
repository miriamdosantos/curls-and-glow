from django.urls import path
from . import views

# Service Page Url
# Home Page Url
urlpatterns = [
    path("", views.home, name="home"),
    path("service/", views.services, name="services"),
]
