from django import forms
from .models import User, Account
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user