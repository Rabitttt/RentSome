from django import forms

from .models import ProductModel

class RentForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "description",
            "price",
            "product_image",
        ]

