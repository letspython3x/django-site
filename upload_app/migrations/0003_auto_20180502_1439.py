# Generated by Django 2.0.4 on 2018-05-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0002_auto_20180502_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
