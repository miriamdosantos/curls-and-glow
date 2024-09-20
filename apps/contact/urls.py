# apps/contact/urls.py

from django.urls import path
from . import views 
urlpatterns = [
   
    
      # Página de contato
    path('admin/messages/', views.admin_message_list, name='admin_message_list'),
    path('admin/respond/<int:message_id>/',  views.admin_respond, name='admin_respond'),  
    path('admin/update-status/<int:message_id>/',  views.update_status, name='update_status'),  
    path('admin/delete-message/<int:message_id>/',  views.delete_message, name='delete_message'),  
    path('contact/',  views.contact, name='contact'),
   
]
