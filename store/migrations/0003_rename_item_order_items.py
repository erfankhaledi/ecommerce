# Generated by Django 4.1.7 on 2023-02-15 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_item_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='items',
        ),
    ]
