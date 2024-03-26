from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label="LOGIN",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="PASSWORD",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))