from django import forms
from config.form import AbstractForm

from general.models import Informasi
from manage_user.models import Customer

class CustomerForm(AbstractForm):
    class Meta:
        model = Customer
        fields = '__all__'