from django.db import models

class CreditCard(models.Model):
    card_number = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()

    def __str__(self):
        return self.card_number

class Loan(models.Model):
    borrower_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.borrower_name} - {self.amount}"
