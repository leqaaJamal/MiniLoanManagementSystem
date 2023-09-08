from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(Provider)
admin.site.register(Loan)
admin.site.register(LoanFund)