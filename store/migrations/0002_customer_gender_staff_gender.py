# Generated by Django 5.1.4 on 2024-12-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="M",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default="M",
                max_length=1,
            ),
        ),
    ]
