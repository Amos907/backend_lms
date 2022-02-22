from rest_framework import serializers
from mpesa_payments.models import C2BMpesaPayment,B2CMpesaPayment,OverduePayments,PaymentsToday

class C2BPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BMpesaPayment
        fields = ['id','mpesa','full_name','name','amount','phone_number']

class B2CPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = B2CMpesaPayment
        fields = ['id','mpesa','full_name','amount','phone_number']

class OverdueSerializer(serializers.ModelSerializer):
    class Meta:
        model  = OverduePayments
        fields = ['id','full_name','loan_amount','amount_due','week_due','days_due']

class PaymentsTodaySerializer(serializers.ModelSerializer):
    class Meta:
        model  = PaymentsToday
        fields = ['id','full_name','loan_amount','installment','week']