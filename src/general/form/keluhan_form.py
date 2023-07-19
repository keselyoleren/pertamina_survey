from django import forms
from config.form import AbstractForm
from general.models import Keluhan



class KeluhanForm(AbstractForm):
    class Meta:
        model = Keluhan
        fields = '__all__'