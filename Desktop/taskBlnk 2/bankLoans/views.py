from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.decorators import api_view
from bankLoans.models import Customer
from bankLoans.serializers import *



@api_view(['POST'])
def LoginUser(request):
    email = request.data["email"]
    password = request.data["password"]
    customer = Customer.objects.filter(email=email, password=password) 
    if(len(customer)>0):
        request.session['user_id'] = customer[0].id
        request.session['user_type'] = "customer"
        return Response("customer:"+str(customer[0].id))
    else:
        bank = Bank.objects.filter(email=email,password=password)
        if(len(bank)>0):
            request.session['user_id'] = bank[0].id
            request.session['user_type'] = "bank"
            return Response("bank:"+str(bank[0].id))
        else:
            provider = Provider.objects.filter(email=email,password=password)
            if(len(provider)>0):
                request.session['user_id'] = provider[0].id
                request.session['user_type'] = "provider"
                return Response("provider:"+str(provider[0].id))
    return Response("user does not exist, please register")


@api_view(['POST'])
def RegisterUser(request):
    type = request.data["userType"]
    info = {}
    serializer = "please choose one of the following types: customer, bank, provider"
    if(type == 'customer'):
        info = {
            'email':request.data["email"],
            'password':request.data["password"]
        }
        serializer = CustomerSerializer(data= info)
        if serializer.is_valid():
            serializer.save()
    elif(type == 'bank'):
        info = {
            'email':request.data["email"],
            'password':request.data["password"],
            'totalFundAmount':request.data["totalFundAmount"]
        }
        serializer = BankSerializer(data= info)
        if serializer.is_valid():
            serializer.save()
    elif(type == 'provider'):
        info = {
            'email':request.data["email"],
            'password':request.data["password"],
        }
        serializer = ProviderSerializer(data=info)
        if serializer.is_valid():
            serializer.save()
    else:
        return Response(serializer)
    #customers = Customer.objects.all()
    return Response(serializer.data)

#bank APIs
@api_view(['POST'])
def createLoan(request):
    if(request.session["user_type"]=="bank"):
        bid = request.session["user_id"]
        loan = {
            'bid': bid,
            'minAmount':request.data["minAmount"],
            'maxAmount':request.data["maxAmount"],
            'interestRate':request.data["interestRate"],
            'duration':request.data["duration"]
        }
        serializer = LoanSerializer(data=loan)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("this user can not do this request")
    
@api_view(['POST'])
def createLoanFund(request):
    if(request.session["user_type"]=="bank"):
        bid = request.session["user_id"]
        loanFund = {
            'bid': bid,
            'minAmount':request.data["minAmount"],
            'maxAmount':request.data["maxAmount"],
            'interestRate':request.data["interestRate"],
            'duration':request.data["duration"]
        }
        serializer = LoanFundSerializer(data=loanFund)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response("this user can not do this request")
  
#providers APIs
@api_view(['POST'])
def providerCreateFund(request):
    if(request.session["user_type"]=="provider"):
        pid = request.session["user_id"]
        provider = Provider.objects.get(id=pid)
        loanFundId = request.data["lid"]
        loanFund = LoanFund.objects.filter(id=loanFundId)
        newAmount = request.data["amount"]
        if(len(loanFund)>0):
            if(loanFund[0].minAmount<=newAmount<=loanFund[0].maxAmount):
                loanFund[0].amount = newAmount
                loanFund[0].pid = provider
                loanFund[0].save()
                bid = BankSerializer(loanFund[0].bid).data["id"]
                bank = Bank.objects.get(id=bid)
                if(bank.totalFundAmount is None):
                   bank.totalFundAmount = 0
                bank.totalFundAmount = bank.totalFundAmount+newAmount
                bank.save()     
                return Response("loan fund has been made")
            else:
                return Response("given fund amount is out of range")
        else:
            return Response("the given loan fund id does not exist")    
    else:
        return Response("this user can not do this request")


#customer APIs
@api_view(['POST'])
def customerChooseLoan(request):
    if(request.session["user_type"]=="customer"):
        cid = request.session["user_id"]
        customer = Customer.objects.get(id=cid)
        loanId = request.data["lid"]
        loan = Loan.objects.filter(id=loanId)
        newAmount = request.data["amount"]
        terms = request.data["terms"]
        if(len(loan)>0):
            if(loan[0].minAmount<=newAmount<=loan[0].maxAmount):
                bid = BankSerializer(loan[0].bid).data["id"]
                bank = Bank.objects.get(id=bid)
                if(bank.totalFundAmount>newAmount):
                    loan[0].amount = newAmount
                    loan[0].cid = customer
                    loan[0].terms = terms
                    loan[0].save()
                    bank.totalFundAmount = bank.totalFundAmount-newAmount
                    bank.save()     
                    return Response("loan has been made")
                else:
                    Response("the requested amount is greater than the total fun amount")
            else:
                return Response("given amount is out of range")
        else:
            return Response("the given loan id does not exist")    
    else:
        return Response("this user can not do this request")

@api_view(['GET'])
def customerViewLoans(request):
    if(request.session["user_type"]=="customer"):
        cid = request.session["user_id"]
        loans = Loan.objects.filter(cid=cid)
        loansArr = []
        for loan in loans:
            serializer = LoanSerializer(loan).data
            loansArr.append(serializer)
        return Response(loansArr)
        
    else:
        return Response("this user can not do this request")



@api_view(['GET'])
def getData(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCustomer(request):
    serializer = CustomerSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def home(request):
    return render(request, 'homePage/home.html')

def contact(request):
    return HttpResponse('Contact page')