# Generated by Django 5.1.1 on 2024-09-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_quotation_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Döküman Adı')),
                ('documant', models.FileField(blank=True, default='', null=True, upload_to='documant/', verbose_name='Döküman')),
                ('link_text', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Link Metni')),
            ],
            options={
                'verbose_name': 'Dökümanlar',
                'verbose_name_plural': 'Dökümanlar',
                'ordering': ['name'],
            },
        ),
    ]
