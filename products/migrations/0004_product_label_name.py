# Generated by Django 3.2.6 on 2021-09-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210929_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
