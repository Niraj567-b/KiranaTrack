# Generated by Django 5.1.4 on 2024-12-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=10)),
                ("AadharNo", models.CharField(max_length=12, unique=True)),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("staffName", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=10)),
                ("address", models.TextField()),
            ],
        ),
    ]