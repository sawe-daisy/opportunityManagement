from django import forms
from .models import User, Account
from django.contrib.auth.hashers import make_password



class RegistrationForm(forms.ModelForm):
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user