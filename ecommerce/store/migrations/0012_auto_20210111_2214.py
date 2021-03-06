# Generated by Django 3.1.5 on 2021-01-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
