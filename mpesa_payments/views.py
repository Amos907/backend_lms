from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date

from mpesa_payments.serializers import C2BPaymentsSerializer,B2CPaymentsSerializer,OverdueSerializer,PaymentsTodaySerializer
from mpesa_payments.models import C2BMpesaPayment,B2CMpesaPayment,OverduePayments,PaymentsToday


class C2BMpesaPaymentView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permision_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        queryset = C2BMpesaPayment.objects.all()
        serializer = C2BPaymentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(selfself, request):
        serializer = C2BPaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTp_204_NO_CONTENT)


class B2CMpesaPaymentView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permision_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        today = time.strftime(r"%Y-%m-%d", time.localtime())
        queryset = B2CMpesaPayment.objects.all()
        serializer = C2BPaymentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(selfself, request):
        serializer = B2CPaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTp_204_NO_CONTENT)

class OverduePaymentsView(APIView):
    def get(self, request):
        queryset = OverduePayments.objects.all()
        serializer = OverdueSerializer(queryset, many=True)
        return Response(serializer.data)

class PaymentsTodayView(APIView):
    def get(self, request):
        today = date.today()
        queryset = PaymentsToday.objects.filter(date = today)
        serializer = PaymentsTodaySerializer(queryset, many=True)
        return Response(serializer.data)
