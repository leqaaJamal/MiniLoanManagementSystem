from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('person/', views.getData),
    path('addCustomer/', views.addCustomer),
    path('register/', views.RegisterUser),
    path('login/', views.LoginUser),
    path('createLoan/', views.createLoan),
    path('createLoanFund/', views.createLoanFund),
    path('providerCreateFund/', views.providerCreateFund),
    path('customerChooseLoan/', views.customerChooseLoan),
    path('customerViewLoans/', views.customerViewLoans),
]