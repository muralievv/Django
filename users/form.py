from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=2)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=2)
    password = forms.CharField(widget=forms.PasswordInput)