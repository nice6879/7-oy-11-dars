from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreditCardViewSet, LoanViewSet
from . import views

router = DefaultRouter()
router.register(r'credit-cards', CreditCardViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
]
