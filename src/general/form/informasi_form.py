from django import forms
from config.form import AbstractForm

from general.models import Informasi

class InformasiForm(AbstractForm):
    class Meta:
        model = Informasi
        fields = '__all__'