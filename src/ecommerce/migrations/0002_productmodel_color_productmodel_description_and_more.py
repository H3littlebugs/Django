# Generated by Django 5.1.2 on 2024-10-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="color",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="productmodel",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="productmodel",
            name="product_dimensions",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="productmodel",
            name="seller",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]