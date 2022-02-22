from django.db.models import F
from loans.models import Loan,LoanType
from .models import C2BMpesaPayment,OverduePayments,PaymentsToday
from datetime import datetime,timedelta
import time
  

def payments_cron_job():
	# This cron job will run once per day...
	today = time.strftime(r"%Y-%m-%d", time.localtime())
	week = 1 
	week_name = "week " + str(week)
	next_payment = loan.date_created.date() + timedelta(7)

	for loan in Loan.objects.filter(complete = False):
		if loan.balance == 0:
			loan.objects.update(complete = True)
		if week < int(loan.payment_plan[0]):
			if today == next_payment:
				paymentsToday = PaymentsToday.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						date = str(next_payment),
						installment = loan.installment,
						week = week_name
					)
				paymentsToday.save()
			elif today == loan.date_created.date() + timedelta(8):
				payment = C2BMpesaPayment.objects.filter(full_name = loan.full_name,week = week,complete = False)
				if payment.exists() != True:
					overdue = OverduePayments.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						week_due = week_name,
						amount_due = loan.installment,
					)
					overdue.save()
					Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount, complete = False).update(overdue_amount = loan.overdue_amount + int(loan.installment))
				else:
					if payment.amount <  loan.installment:
						amount_due = int(loan.installment) - int(payment.amount)
						overdue = OverduePayments.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						week_due = week_name,
						amount_due = amount_due,
						) 
						overdue.save()
						Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(overdue_amount = loan.overdue_amount + amount_due
					else if payment.amount > loan.installment:
						overpaid = payment.amount - loan.installment
						Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(installment  = overpaid)
			week = week + 1
			next_payment = next_payment + timedelta(7)

		else if week == int(loan.payment_plan[0]):
			next_payment = loan.date_created.date() + timedelta(7)
			if today == next_payment:
				paymentsToday = PaymentsToday.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						date = str(next_payment),
						installment = loan.installment,
						week = week_name
					)
				paymentsToday.save()
			else if today == loan.date_created.date() + timedelta(8):
				payment = C2BMpesaPayment.objects.filter(full_name = loan.full_name,week = week,complete = False)
				if payment.exists() != True:
					overdue = OverduePayments.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						week_due = week_name,
						amount_due = loan.installment,
					)
					overdue.save()
					Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(overdue_amount = loan.overdue_amount + int(loan.installment))
				else if payment.exists() == True:
					if payment.amount <  loan.installment:
						amount_due = int(loan.installment) - int(payment.amount)
						overdue = OverduePayments.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						week_due = week_name,
						amount_due = amount_due,
						) 
						overdue.save()
						Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount).update(overdue_amount = loan.overdue_amount + amount_due)

				else if payment.exists() == True and loan.amount_due == 0: 
					Loan.objects.filter(full_name = loan.full_name,loan_amount = loan.loan_amount,complete = False).update(complete = True)
					for i in C2BMpesaPayment.objects.filter(full_name = loan.full_name,complete = False):
						i.update(complete = True)


def overdue_status():
	# This cron job runs daily after five minutes...
	for overdue in OverduePayments.objects.all():
		for payment in C2BMpesaPayment.objects.filter(complete = False):
			if overdue.full_name == payment.full_name and overdue.week_due == payment.week:
				loans = Loan.objects.get(full_name = payment.full_name)
				if payment.amount == overdue.amount_due:
					OverduePayments.objects.filter(full_name = payment.full_name,week_due = payment.week).delete()

				else if payment.amount < overdue.amount_due:
					amount_due = int(loans.installment) - int(payment.amount)
					OverduePayments.objects.filter(full_name = payment.full_name,week_due = payment.week).update(amount_due = amount_due)
					 

def increment_days():
	# This cron job will run once a day...
	OverduePayments.objects.all().update(days_due = F('days_due')+1)

def check_balance():
	# This cron job will run every minute...
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
    

				 


	


 


