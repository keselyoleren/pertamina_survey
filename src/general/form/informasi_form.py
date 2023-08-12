from django import forms
from config.form import AbstractForm

from general.models import Informasi, InformasiPenerbangan

class InformasiForm(AbstractForm):
    class Meta:
        model = Informasi
        fields = '__all__'

class InformasiPenerbanganForm(AbstractForm):
    waktu = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'type':'datetime-local',
        })
    )

    
    class Meta:
        model = InformasiPenerbangan
        fields = '__all__'
