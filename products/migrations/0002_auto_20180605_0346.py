# Generated by Django 2.0.5 on 2018-06-04 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(upload_to='images/icons/'),
        ),
    ]