# Generated by Django 5.1.3 on 2024-11-12 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='customer_number',
            new_name='customer_name',
        ),
    ]