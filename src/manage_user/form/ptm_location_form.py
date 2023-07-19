from django import forms
from config.form import AbstractForm

from general.models import Informasi
from manage_user.models import PTM, Customer

class PTMForm(AbstractForm):
    class Meta:
        model = PTM
        fields = '__all__'