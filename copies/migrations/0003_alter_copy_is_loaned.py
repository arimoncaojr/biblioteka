# Generated by Django 4.1.7 on 2023-03-08 22:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="copy",
            name="is_loaned",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]