from django import forms
from .models import User, Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password



class RegistrationForm(UserCreationForm):
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)
    class Meta:
        model = User
        fields = ['firstName', 'username', 'email']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user