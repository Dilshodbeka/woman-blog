from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', 
                               widget=forms.TextInput(attrs={'class': 'form-input'})
                               )
    password = forms.CharField(label='Parol', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'})
                               )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', 
                               widget=forms.TextInput(attrs={'class': 'form-input'})
                               )
    password1 = forms.CharField(label='Parol', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'})
                               )
    password2 = forms.CharField(label='Parolni qaytaring', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'})
                               )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username': 'Ismingiz',
            'email': 'Email',
            'first_name': 'Ismingiz',
            'last_name': 'Familiyangiz',
            'password1': 'Parol',
            'password2': 'Parolni qaytaring',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Parollar bir xil emas')
        return data['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email band')
        return email
    

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(label='Login', disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', disabled=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'first_name': 'Ismingiz',
            'last_name': 'Familiyangiz',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='New password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

