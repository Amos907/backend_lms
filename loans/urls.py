from .views import LoansView,LoanTypeView
from django.urls import path

urlpatterns = [
    path('loans/', LoansView.as_view(), name='loans'),
    path('loan-products/',LoanTypeView.as_view(),name = 'loan-type'),
    path('loan-products/delete/<int:id>/',LoanTypeView.as_view(),name = 'delete'),
]
