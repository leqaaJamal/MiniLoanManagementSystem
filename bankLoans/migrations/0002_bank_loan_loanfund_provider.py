# Generated by Django 3.2.18 on 2023-03-08 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankLoans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=8)),
                ('totalFundAmount', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='LoanFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minAmount', models.FloatField(null=True)),
                ('maxAmount', models.FloatField(null=True)),
                ('interestRate', models.FloatField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('amount', models.FloatField(null=True)),
                ('bid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bankLoans.bank')),
                ('pid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankLoans.provider')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minAmount', models.FloatField(null=True)),
                ('maxAmount', models.FloatField(null=True)),
                ('interestRate', models.FloatField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('terms', models.CharField(max_length=500)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankLoans.bank')),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankLoans.customer')),
            ],
        ),
    ]
