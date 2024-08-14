from rest_framework import viewsets
from .models import CreditCard, Loan
from .serializers import CreditCardSerializer, LoanSerializer
from django.shortcuts import render

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


def index(request):
    return render(request, 'lending/index.html')