from django.core.management.base import BaseCommand
from django.db.models import F
from loans.models import Loan,LoanType
from mpesa_payments.models import C2BMpesaPayment,OverduePayments,PaymentsToday
from datetime import datetime,timedelta
import time

class Command(BaseCommand):
	help = 'update loan balances'

	def handle(self,*args,**kwargs):
		paid_amount = 0
		total_amount = 0

		loans = Loan.objects.filter(complete = False)
		 
		for loan in loans:
			payment = loan.c2bmpesapayment_set.all()
			if payment:
				for x in payment:
					paid_amount = paid_amount + int(x.amount)
				balance_2 = loan.total - paid_amount
				Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(total_balance = balance_2)
			else:
				Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(total_balance = loan.total)		 
				
			paid_amount = 0
		self.stdout.write("Balances Updated Succesfully")

