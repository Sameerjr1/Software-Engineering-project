# Generated by Django 3.1.5 on 2021-01-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cetegory',
            field=models.CharField(choices=[('S', 'Shirt'), ('M', 'Mobile Phone')], max_length=100),
        ),
    ]
