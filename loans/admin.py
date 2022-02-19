from django.contrib import admin
from django.db.models import fields
from .models import LoanType, Loan


class LoanAdminSite(admin.ModelAdmin):
    model = Loan
    fields = ['id','user','full_name', 'loan_amount','date_created','payment_plan','installment','total_balance','overdue_amount','complete','initial_installment',]
    list_display = ('id','user','full_name','loan_amount','payment_plan','installment','total_balance','overdue_amount','complete','initial_installment')

    readonly_fields = ['date_created','id']

class LoanTypeAdminSite(admin.ModelAdmin):
    model = LoanType
    fields = ['id','loan_amount','four_weeks','five_weeks','seven_weeks','eight_weeks','ten_weeks','status']
    list_display = ('id','loan_amount','four_weeks',
                    'five_weeks','seven_weeks',
                    'eight_weeks','ten_weeks','status','get_num_customers')

    readonly_fields = ['id','get_num_customers']

admin.site.register(LoanType,LoanTypeAdminSite)
admin.site.register(Loan, LoanAdminSite)
# Register your models here.
