# Generated by Django 3.2.8 on 2021-10-29 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211026_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='track_list1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='track_list2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='track_list3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='track_list4',
        ),
    ]
