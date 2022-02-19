from rest_framework import serializers
from .models import Loan,LoanType
 
class LoanSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField(source='disbursedDate')
    # balance_rem = serializers.ReadOnlyField(source = 'balance')
    class Meta:
        model = Loan
        fields = ['id','user','full_name', 'loan_amount',
                  'date','payment_plan','installment','total_balance','overdue_amount','initial_installment','complete']

class LoanTypeSerializer(serializers.ModelSerializer):
    num_customers = serializers.ReadOnlyField(source = 'get_num_customers')
    class Meta:
        model = LoanType
        
        fields = ['id','loan_amount','four_weeks','five_weeks','seven_weeks','eight_weeks','ten_weeks','status','num_customers']