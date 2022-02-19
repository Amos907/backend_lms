from django.db import models
from mpesa_payments.models import C2BMpesaPayment
# Create your models here.

class LoanType(models.Model):
    id = models.AutoField(primary_key=True)
    loan_amount = models.CharField(
        max_length=200,null = True,blank =True)
    four_weeks = models.CharField(max_length = 200, null =True, blank =True)
    five_weeks = models.CharField(max_length = 200, null =True, blank =True)
    seven_weeks = models.CharField(max_length = 200, null =True, blank =True)
    eight_weeks = models.CharField(max_length = 200, null =True, blank =True)
    ten_weeks = models.CharField(max_length = 200, null =True, blank =True)
    status = models.CharField(default = "active",max_length = 200)


    def get_num_customers(self):
        num = 0
        for amount in range(3000,41000,1000):
            print
            if int(self.loan_amount) == amount:
                loan = Loan()
                num = loan.get_customers(amount)

        return num

    def __str__(self):
        return self.loan_amount

class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length = 200, null = True, blank = True)
    full_name = models.CharField(max_length = 200,null = True,blank = True)
    loan_amount = models.CharField(max_length = 200, null =True,blank  =True)
    payment_plan = models.CharField(max_length = 200, default = "4 Weeks",null =True, blank =True)
    installment = models.CharField(max_length = 200,null = True,blank = True)
    initial_installment = models.CharField(max_length = 200,null = True,blank = True)
    date_created = models.DateTimeField(
        auto_now=True)
    complete = models.BooleanField(default = False)
    overdue_amount = models.IntegerField(default = 0)
    total_balance = models.IntegerField(default = 0)



    def __str__(self):
        return self.user

    def disbursedDate(self):
        date = self.date_created.date()
        return date

    def get_customers(self,amount):
        num = 0
        for i in Loan.objects.filter(loan_amount = str(amount)):
            num += 1
        return num


    # def balance(self):
    #     paid_amount = 0
    #     balance = 0
    #     loans = Loan.objects.filter(complete = False)

    #     for loan in loans:
    #         payment = C2BMpesaPayment.objects.filter(full_name = loan.full_name,complete = False)
    #         if payment.exists():
    #             for x in payment:
    #                 total_amount = int(loan.initial_installment) * int(loan.payment_plan[0])
    #                 paid_amount = paid_amount + int(x.amount)
    #                 balance = total_amount - paid_amount        

    #         else:
    #             balance = total_amount
    #     return balance

    @property
    def get_date_created(self):
        return self.date_created.date()

    @property
    def get_name(self):
        return self.full_name

    @property
    def get_payment_plan(self):
        return self.payment_plan

    @property
    def get_loan_amount(self):
        return self.loan_amount
     
     
    
    
