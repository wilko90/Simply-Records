# Generated by Django 3.2.8 on 2021-10-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_formats',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
