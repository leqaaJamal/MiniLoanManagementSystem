# Generated by Django 3.2.18 on 2023-03-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankLoans', '0003_auto_20230308_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
