from django.core.management.base import BaseCommand
from django.db.models import F
from loans.models import Loan,LoanType
from mpesa_payments.models import C2BMpesaPayment,OverduePayments,PaymentsToday
from datetime import datetime,timedelta
import time

class Command(BaseCommand):
	help = 'Handle Overdue'

	def handle(self,*args,**kwargs):
		today = time.strftime(r"%Y-%m-%d", time.localtime())
		week = 1 
		week_name = "week " + str(week)
		 
		payment_overdue = today

		OverduePayments.objects.all().update(days_due = F('days_due')+1)

		for loan in Loan.objects.filter(complete = False):
			while week < int(loan.payment_plan[0]):
				payment_overdue = loan.date_created.date() + timedelta(8)

				if today ==  str(payment_overdue):
					payment = loan.c2bmpesapayment_set.filter(complete = False)
					if payment:
						for i in payment:
							if i.amount <  loan.installment:
								amount = int(i.amount) - int(loan.installment)
								overdue = OverduePayments.objects.create(
								full_name = loan.full_name,
								loan_amount = loan.loan_amount,
								week_due = week_name,
								amount_due = amount
								) 
								overdue.save()
								Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(overdue_amount = amount,installment = amount + int(loan.initial_installment))
							elif i.amount > loan.installment:
								overpaid = int(i.amount) - int(loan.installment)
								Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(installment  = overpaid)
							
					else:
						overdue = OverduePayments.objects.create(
							full_name = loan.full_name,
							loan_amount = loan.loan_amount,
							week_due = week_name,
							amount_due = loan.installment,
						)
						overdue.save()
						Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(overdue_amount = loan.overdue_amount + int(loan.installment))
		week = week + 1
		payment_overdue = payment_overdue + timedelta(8)
		 
		self.stdout.write("Overdues Updated Succesfully")
