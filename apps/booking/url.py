from django.urls import path
from . import views 

urlpatterns = [
    path('', views.make_appointment, name='booking'),
    path('select_time/', views.select_date, name = 'select_time'),
    path('book-appointment/', views.book_appointment, name='book_appointment')
]
