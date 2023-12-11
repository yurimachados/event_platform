# Generated by Django 4.2.6 on 2023-12-10 05:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("core", "0005_alter_comment_options_alter_company_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="customer_groups", to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                related_name="customer_user_permissions",
                to="auth.permission",
            ),
        ),
        migrations.AlterField(
            model_name="manager",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="manager_groups", to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="manager",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                related_name="manager_user_permissions",
                to="auth.permission",
            ),
        ),
    ]