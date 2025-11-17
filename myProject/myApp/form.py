from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['ename', 'desg', 'salary', 'image']
        widgets = {
            'ename': forms.TextInput(attrs={'class': 'form-control'}),
            'desg': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }