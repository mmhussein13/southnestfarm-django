# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    """Form for user registration."""
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': ' Repeat Password',
        'class': 'form-control border-0',  # Added class for styling
    }))
    
    class Meta:
        model = Account
        fields = [
            'first_name', 'last_name',
            'phone_number', 'email', 'password', 'confirm_password'  # Included confirm_password
        ]

    def clean(self):
        """Validate that the two password fields match."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match. Please try again.")
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = ' Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = ' Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = ' Enter Email '
        self.fields['phone_number'].widget.attrs['placeholder'] = ' Enter Phone Number '
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control border-0'  # Apply CSS across all fields
            