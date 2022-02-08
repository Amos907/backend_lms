from django.urls import path
from mpesa_payments.views import C2BMpesaPaymentView,B2CMpesaPaymentView,OverduePaymentsView,PaymentsTodayView
urlpatterns = [
    path('c2b/', C2BMpesaPaymentView.as_view(), name='loans'),
    path('b2c/', B2CMpesaPaymentView.as_view(), name='loans'),
    path('overdue/',OverduePaymentsView.as_view(),name = 'overdue'),
    path('payments-today/',PaymentsTodayView.as_view(),name = 'payments-today')
]


