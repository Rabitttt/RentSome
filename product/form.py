from time import timezone
from django import forms
from .models import ProductModel
from datetime import datetime

class RentForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "description",
            "price",
            "product_image",
        ]

class DateForm(forms.Form):
    hire_end_date = forms.DateField(widget=forms.SelectDateWidget())
