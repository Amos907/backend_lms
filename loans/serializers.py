from rest_framework import serializers
from .models import Loan,LoanType
 
class LoanSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField(source='disbursedDate')
    class Meta:
        model = Loan
        fields = ['id','user','full_name', 'loan_amount',
                  'date','payment_plan','installment']

class LoanTypeSerializer(serializers.ModelSerializer):
    num_customers = serializers.ReadOnlyField(source = 'get_num_customers')
    class Meta:
        model = LoanType
        
        fields = ['id','loan_amount','four_weeks','five_weeks','seven_weeks','eight_weeks','ten_weeks','status','num_customers']