from django.db.models import F
from loans.models import Loan,LoanType
from .models import C2BMpesaPayment,OverduePayments,PaymentsToday
from datetime import datetime,timedelta
import time
  

def payments_cron_job():
	# This cron job will run once per day...
	today = time.strftime(r"%Y-%m-%d", time.localtime())
	week = 1
	next_payment = today 
	week_name = "week " + str(week)

	for loan in Loan.objects.all():
		while week <= int(loan.payment_plan[0]):
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
			elif today == loan.date_created.date() + timedelta(8):
				payment = C2BMpesaPayment.objects.filter(full_name = loan.full_name,week = week)
				if payment.exists() != True:
					overdue = OverduePayments.objects.create(
						full_name = loan.full_name,
						loan_amount = loan.loan_amount,
						week_due = week_name,
						amount_due = loan.installment,
					)
					overdue.save()
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
			week = week + 1
			next_payment = next_payment + timedelta(7)

def overdue_status():
	# This cron job runs daily after five minutes...
	for overdue in OverduePayments.objects.all():
		for payment in C2BMpesaPayment.objects.all():
			if overdue.full_name == payment.full_name and overdue.week_due == payment.week:
				loans = Loan.objects.get(full_name = payment.full_name)
				if payment.amount == overdue.amount_due:
					OverduePayments.objects.filter(full_name = payment.full_name,week_due = payment.week).delete()

				elif payment.amount < overdue.amount_due:
					amount_due = int(loans.installment) - int(payment.amount)
					OverduePayments.objects.filter(full_name = payment.full_name,week_due = payment.week).update(amount_due = amount_due)
					 

def increment_days():
	# This cron job will ru once a day...
	OverduePayments.objects.all().update(days_due = F('days_due')+1)


 


