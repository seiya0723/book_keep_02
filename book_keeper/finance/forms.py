from django import forms 

from .models import Category,Balance

class BalanceForm(forms.ModelForm):

    class Meta:
        model   = Balance
        fields  = [ "category","pay_dt","value" ]


class CategoryForm(forms.ModelForm):

    class Meta:
        model   = Category
        fields  = [ "name","income" ]

