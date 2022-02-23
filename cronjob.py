# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from mpesa_payments.cron import check_balance

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(check_balance, "interval", seconds=30)

scheduler.start()