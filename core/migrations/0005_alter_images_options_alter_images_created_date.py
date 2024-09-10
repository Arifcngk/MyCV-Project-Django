# Generated by Django 5.1.1 on 2024-09-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['name'], 'verbose_name': 'Images Setting', 'verbose_name_plural': 'Images Settings'},
        ),
        migrations.AlterField(
            model_name='images',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]