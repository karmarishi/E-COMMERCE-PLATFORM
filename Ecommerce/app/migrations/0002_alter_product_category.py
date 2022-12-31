# Generated by Django 4.1.2 on 2022-12-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("M", "Mobiles"),
                    ("L", "Laptop"),
                    ("TW", "Top Wear"),
                    ("BW", "Bottom Wear"),
                ],
                max_length=2,
            ),
        ),
    ]