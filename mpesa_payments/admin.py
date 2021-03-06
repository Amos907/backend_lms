from django.contrib import admin
from mpesa_payments.models import C2BMpesaPayment,B2CMpesaPayment,OverduePayments,PaymentsToday


class C2BMpesaAdminSite(admin.ModelAdmin):
    model = C2BMpesaPayment

    fields = ['id','mpesa','full_name','name', 'amount', 'phone_number','week','complete']
    list_display = ('id','mpesa','full_name','name', 'amount', 'phone_number','week','complete')
    readonly_fields = ['id']

class B2CMpesaAdminSite(admin.ModelAdmin):
    model = B2CMpesaPayment
    fields = ['id','mpesa','full_name', 'amount', 'phone_number']
    list_display = ('id','mpesa','full_name', 'amount', 'phone_number')

    readonly_fields = ['id']

class OverdueAdminSite(admin.ModelAdmin):
    model = OverduePayments
    fields = ['id','full_name','loan_amount', 'amount_due', 'week_due','days_due']
    list_display = ('id','full_name','loan_amount', 'amount_due', 'week_due','days_due')

    readonly_fields = ['id']

class PaymentsTodayAdminSite(admin.ModelAdmin):
    model = PaymentsToday
    fields = ['id','full_name','date', 'installment', 'week','loan_amount']
    list_display = ('id','full_name','loan_amount','date', 'installment', 'week','loan_amount')

    readonly_fields = ['id']



admin.site.register(C2BMpesaPayment,C2BMpesaAdminSite)
admin.site.register(B2CMpesaPayment,B2CMpesaAdminSite)
admin.site.register(OverduePayments,OverdueAdminSite)
admin.site.register(PaymentsToday,PaymentsTodayAdminSite)
 
