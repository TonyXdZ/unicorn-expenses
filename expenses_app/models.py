from email.policy import default
from django.db import models
from django.utils import timezone


class Expense(models.Model): 
    short_name = models.CharField(max_length=255)
    description = models.TextField()
    amount_spent = models.PositiveIntegerField()
    date_spent = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Expense {self.short_name}'
