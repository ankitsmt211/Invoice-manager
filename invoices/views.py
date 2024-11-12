from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from invoices.models import Invoice, InvoiceDetails


class SerializerInvoiceDetails(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = ['description', 'quantity', 'price', 'line_total']


class SerializerInvoice(serializers.ModelSerializer):
    date = serializers.DateField(source='invoice_date')
    details = SerializerInvoiceDetails(many=True)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        details = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)

        for detail in details:
            InvoiceDetails.objects.create(invoice=invoice, **detail)

        return invoice

    def update(self, instance, validated_data):
        details = validated_data.pop('details')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # assumed replacing meant that we remove older instances
        existing_details = InvoiceDetails.objects.filter(invoice=instance).all()
        if existing_details:
            existing_details.delete()
        for detail in details:
            InvoiceDetails.objects.create(invoice=instance, **detail)

        return instance


@api_view(["POST", "PUT"])
def create_or_update_invoice(request, *args, **kwargs):
    # would prefer separate views if URLs were not same
    if request.method == "POST":
        serializer = SerializerInvoice(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response("created invoice successfully", status=status.HTTP_201_CREATED)
    elif request.method == "PUT":
        invoice_obj = Invoice.objects.filter(invoice_number=request.data.get('invoice_number')).first()
        if not invoice_obj:
            return Response("Invoice does not exist, please try with valid Invoice ID")

        serializer = SerializerInvoice(data=request.data, instance=invoice_obj, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response("updated invoice successfully", status=status.HTTP_200_OK)

