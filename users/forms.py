from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'date_of_birth']

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Example23@gmail.com', 'class': 'form-control'}),
        max_length=255
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '******', 'class': 'form-control'}),
    )
    
    date_of_birth = forms.DateField(
            widget=forms.DateInput(attrs={'placeholder': '25/12/1990', 'class': 'form-control'}),
            required=False,
            input_formats=['%d/%m/%Y'],  
        )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '******', 'class': 'form-control'}),
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Example23@gmail.com', 'class': 'form-control'}),
        max_length=255
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '******', 'class': 'form-control'}),
    )
