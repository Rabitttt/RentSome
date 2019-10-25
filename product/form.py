from django import forms


class RentForm(forms.Form):
    name = forms.CharField(max_length=50,label="Ürün Adı")
    price = forms.FloatField(label="Fiyat")