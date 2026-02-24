from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'sender_name', 'sender_account', 'sender_country',
            'receiver_name', 'receiver_account', 'receiver_country',
            'receiver_email', 'amount',  'receiver_bank'
        ]
        widgets = {
            'sender_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter sender full name',
                'required': True
            }),
            'sender_account': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter account number',
                'required': True
            }),
            'sender_country': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter country',
                'required': True
            }),
            'receiver_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter receiver full name',
                'required': True
            }),
            'receiver_account': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter account number',
                'required': True
            }),
            'receiver_country': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter country',
                'required': True
            }),
            'receiver_email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter email address',
                'required': True
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': '0.00', 
                'step': '0.01',
                'required': True,
                'min': '0.01'
            }),


            'receiver_bank': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'bank',
                'required': True
            }),
            
        }
    
    def clean_sender_account(self):
        account = self.cleaned_data.get('sender_account')
        if not account:
            raise ValidationError("Sender account number is required")
        if not account.isdigit():
            raise ValidationError("Account number must contain only digits")
        if len(account) < 10:
            raise ValidationError("Account number must be at least 10 digits")
        return account
    
    def clean_receiver_account(self):
        account = self.cleaned_data.get('receiver_account')
        if not account:
            raise ValidationError("Receiver account number is required")
        if not account.isdigit():
            raise ValidationError("Account number must contain only digits")
        if len(account) < 10:
            raise ValidationError("Account number must be at least 10 digits")
        return account
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if not amount:
            raise ValidationError("Amount is required")
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero")
        return amount