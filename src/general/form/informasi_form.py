from django import forms
from config.form import AbstractForm

from general.models import Informasi, InformasiPenerbangan

class InformasiForm(AbstractForm):
    class Meta:
        model = Informasi
        fields = '__all__'

class InformasiPenerbanganForm(AbstractForm):
    class Meta:
        model = InformasiPenerbangan
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(InformasiPenerbanganForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'user':
                self.fields['user'].widget = forms.HiddenInput()