from django import forms
from shop.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.forms import widgets


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name...', 'required': True}))
    note = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your note', 'required': True}))
    active = forms.BooleanField(required=True)

    class Meta:
        model = Customer
        fields = ['name', 'email', 'note', 'active']

    def validate(self, value):
        super().validate(value)
        for email in value:
            validate_email(email)
