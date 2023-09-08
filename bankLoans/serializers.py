#convert from objects to datatypes so response object can understand it.
from rest_framework import serializers
from bankLoans.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__' 

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__' 

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__' 

class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = '__all__' 