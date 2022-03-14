from django.core.management.base import BaseCommand
from django.db.models import F
from loans.models import Loan,LoanType
from mpesa_payments.models import C2BMpesaPayment,OverduePayments,PaymentsToday
from datetime import datetime,timedelta
import time

class Command(BaseCommand):
	help = 'update loan balances'

	def handle(self,*args,**kwargs):
		for overdue in OverduePayments.objects.all():
			for payment in C2BMpesaPayment.objects.filter(complete = False):
				if overdue.full_name == payment.full_name and overdue.week_due == payment.week:
					loans = Loan.objects.get(user = payment.full_name)
					if payment.amount == overdue.amount_due:
						OverduePayments.objects.filter(full_name = payment.full_name,week_due = payment.week).delete()

					elif payment.amount < overdue.amount_due:
						amount_due = int(loans.installment) - int(payment.amount)
						OverduePayments.objects.filter(full_name = payment.full_name,week_due = payment.week).update(amount_due = amount_due)
						 
		self.stdout.write("Balances Updated Succesfully")

