from django import forms
from expenses_app.models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['short_name',
                'description',
                'amount_spent']