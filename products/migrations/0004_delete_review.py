# Generated by Django 3.2 on 2023-04-03 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
