# Generated by Django 4.2 on 2023-04-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0026_auto_20200628_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='cover',
        ),
        migrations.AddField(
            model_name='buku',
            name='dokumen',
            field=models.FileField(null=True, upload_to='cover/'),
        ),
    ]
