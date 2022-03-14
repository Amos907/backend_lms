from django.core.management.base import BaseCommand
from django.db.models import F
from loans.models import Loan,LoanType
from mpesa_payments.models import C2BMpesaPayment,OverduePayments,PaymentsToday
from datetime import datetime,timedelta
import time

class Command(BaseCommand):
	help = 'Handle Last Day'

	def handle(self,*args,**kwargs):
		today = time.strftime(r"%Y-%m-%d", time.localtime())
		week = int(loans.payment_plan[0])
		week_name = "week " + str(week)
		 

		for loan in Loan.objects.filter(complete = False):
			while week >= int(loans.payment_plan[0]):
				if today == str(loan.date_created.date() + timedelta(8)):
					payment = loan.c2bmpesapayment_set.filter(complete = False,week = week)
					if payment.exists() != True:
						if OverduePayments.objects.filter(full_name = loan.full_name,week = week_name,complete = False):
							pass
						else:
							overdue = OverduePayments.objects.create(
								full_name = loan.full_name,
								loan_amount = loan.loan_amount,
								week_due = week_name,
								amount_due = loan.installment,
							)
							overdue.save()
							Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(overdue_amount = loan.installment)
					elif payment.exists() == True:
						if payment.amount <  loan.installment:
							amount_due = int(loan.installment) - int(payment.amount)
							if OverduePayments.objects.filter(full_name = loan.full_name,week = week_name,complete = False,amount_due = amount_due):
								pass
							else:

								overdue = OverduePayments.objects.create(
								full_name = loan.full_name,
								loan_amount = loan.loan_amount,
								week_due = week_name,
								amount_due = amount_due,
								) 
								overdue.save()
								Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount).update(overdue_amount = loan.overdue_amount + amount_due)

					elif payment.exists() == True and loan.amount_due == 0: 
						Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(complete = True)
						for i in C2BMpesaPayment.objects.filter(full_name = loan.full_name,complete = False):
							i.update(complete = True)
		self.stdout.write("Last Day Updated Succesfully")

