# Generated by Django 3.1.5 on 2021-01-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210108_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
            preserve_default=False,
        ),
    ]
