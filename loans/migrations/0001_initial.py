# Generated by Django 4.1.7 on 2023-03-08 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loan",
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
                ("date_collected", models.DateTimeField(auto_now_add=True)),
                ("date_limit_return", models.DateTimeField(blank=True, null=True)),
                ("date_returned", models.DateTimeField(blank=True, null=True)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loans_books",
                        to="copies.copy",
                    ),
                ),
            ],
        ),
    ]