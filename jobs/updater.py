from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from mpesa_payments.cron import check_balance

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(check_balance, "interval", seconds=30)
	scheduler.start()