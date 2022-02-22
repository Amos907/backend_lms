from django.db import models
from loans.models import Loan

class C2BMpesaPayment(models.Model):
    id = models.AutoField(primary_key = True)
    mpesa = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length = 200,null = True,blank = True)
    full_name = models.ForeignKey(Loan,on_delete = models.CASCADE,blank = True,null = True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length = 200,null = True,blank = True)
    date_created = models.DateTimeField(
        auto_now=True)
    amount = models.CharField(max_length = 200, null =True,blank  =True)
    phone_number = models.CharField(max_length = 200,null = True,blank = True)
    date_created = models.DateTimeField(
        auto_now=True)
    week = models.CharField(max_length = 200,null = True,blank = True)
    complete = models.BooleanField(default = False)
    
class B2CMpesaPayment(models.Model):
    id = models.AutoField(primary_key = True)
    mpesa = models.CharField(max_length=200, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length = 200,null = True,blank = True)
    date_created = models.DateTimeField(
        auto_now=True)
    amount = models.CharField(max_length = 200, null =True,blank  =True)
    phone_number = models.CharField(max_length = 200,null = True,blank = True)
    date_created = models.DateTimeField(
        auto_now=True)

class OverduePayments(models.Model):
    id = models.AutoField(primary_key = True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    loan_amount = models.CharField(max_length = 200, null =True,blank  =True)
    amount_due = models.CharField(max_length = 200, null =True,blank  =True)
    week_due = models.CharField(max_length = 200,null = True,blank = True)
    days_due = models.IntegerField(default = 1)
    complete = models.BooleanField(default = False)

class PaymentsToday(models.Model):
    id = models.AutoField(primary_key = True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    loan_amount = models.CharField(max_length = 200, null =True,blank  =True)
    date = models.CharField(max_length = 200,null =True,blank = True)
    installment = models.CharField(max_length = 200,null = True,blank = True)
    week = models.CharField(max_length = 200,null =True,blank =True)