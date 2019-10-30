from django import forms
from django.forms import ModelForm
from .models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label='Kullanıcı Adı')
    password = forms.CharField(widget=forms.PasswordInput,max_length=20,label="Parola")
    confirm = forms.CharField(widget=forms.PasswordInput,max_length=20,label="Parolayı Onayla")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolarar Eşleşmiyor")

        values = {
            "username" : username,
            "password" : password
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(widget=forms.PasswordInput,label="Parola")

class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'location',
            'profile_picture',
            'money',
        ]