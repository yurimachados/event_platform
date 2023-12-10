# Generated by Django 4.2.6 on 2023-12-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="cover",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/company_covers/"
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/company_images/"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="cover",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/event_covers/"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/event_images/"
            ),
        ),
    ]
