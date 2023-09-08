from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=8)


class Bank(models.Model):
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=8)
    totalFundAmount = models.FloatField(null=True)

class Provider(models.Model):
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=8)

class Loan(models.Model):
    bid = models.ForeignKey(Bank, on_delete=models.CASCADE)
    cid = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    minAmount = models.FloatField(null=True)
    maxAmount = models.FloatField(null=True)
    interestRate = models.FloatField(null=True)
    duration = models.IntegerField(null=True)
    terms = models.CharField(max_length=500, null=True)
    amount = models.CharField(max_length=500, null=True)


class LoanFund(models.Model):
    bid = models.ForeignKey(Bank, null=True, on_delete=models.CASCADE)
    pid = models.ForeignKey(Provider, null=True, on_delete=models.SET_NULL)
    minAmount = models.FloatField(null=True)
    maxAmount = models.FloatField(null=True)
    interestRate = models.FloatField(null=True)
    duration = models.IntegerField(null=True)
    amount = models.FloatField(null=True)
