# Generated by Django 5.1.1 on 2024-09-10 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_quotation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quotation',
            new_name='Quotes',
        ),
    ]
