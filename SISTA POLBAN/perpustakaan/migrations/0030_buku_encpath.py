# Generated by Django 4.0.3 on 2023-04-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0029_buku_key_enkripsi_alter_buku_dokumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='encpath',
            field=models.CharField(max_length=100, null=True),
        ),
    ]