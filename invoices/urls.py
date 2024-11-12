from django.urls import path

from invoices.views import create_or_update_invoice

urlpatterns = [
    path('', create_or_update_invoice),
]