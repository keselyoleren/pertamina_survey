
from pyexpat import model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

from config.form import AbstractForm
from manage_user.models import AccountUser

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control', 'pnameholder': 'Password'}),
    )

    
    
class ProfileForm(AbstractForm):
    class Meta:
        model = AccountUser
        fields = ['username', 'email', 'first_name', 'last_name', 'ptm_location', 'profile_picture']
        