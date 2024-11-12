import uuid

from django.db import models


# Create your models here.

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_number = models.CharField(max_length=255, unique=True)
    customer_name = models.CharField(max_length=255)
    invoice_date = models.DateField()


class InvoiceDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20,decimal_places=2)
    line_total = models.DecimalField(max_digits=20, decimal_places=2)
