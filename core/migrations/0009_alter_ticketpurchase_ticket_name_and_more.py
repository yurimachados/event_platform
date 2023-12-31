# Generated by Django 4.2.6 on 2023-12-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_ticketpurchase_ticket_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketpurchase",
            name="ticket_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="ticketpurchase",
            name="ticket_price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
