# Generated by Django 4.1.5 on 2023-01-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("call_number", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("year", models.CharField(max_length=50)),
                ("publisher", models.CharField(max_length=100)),
                ("isbn", models.CharField(max_length=100)),
                ("inventory", models.CharField(max_length=50)),
                ("language", models.CharField(max_length=100)),
                ("notes", models.TextField(null=True)),
            ],
        ),
    ]