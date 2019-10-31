from django.urls import path
from .views import read_clients, new_client, edit_client, delete_client

urlpatterns = [
    path('clients/', read_clients, name='clients'),
    path('new-client/', new_client, name='new_client'),
    path('edit/<int:id>', edit_client, name='edit_client'),
    path('delete/<int:id>', delete_client, name='delete_client'),
]
