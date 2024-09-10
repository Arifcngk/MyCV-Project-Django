# Generated by Django 5.1.1 on 2024-09-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Resim Alanı')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/', verbose_name='Resim')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
            ],
        ),
    ]