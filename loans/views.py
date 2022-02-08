from django.shortcuts import render
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoanSerializer,LoanTypeSerializer
from .models import Loan,LoanType


class LoansView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permision_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        queryset = Loan.objects.all()
        serializer = LoanSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanTypeView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permision_classes = [permissions.IsAuthenticated, ]

    def get_object(self, id):
        try:
            return LoanType.objects.get(id=id)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        queryset = LoanType.objects.all()
        serializer = LoanTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(selfself,request):
        serializer = LoanTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# Create your views here.

 
    
