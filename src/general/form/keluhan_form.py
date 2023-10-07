from django import forms
from config.form import AbstractForm
from general.models import Keluhan, Tanggapan



class KeluhanForm(AbstractForm):
    class Meta:
        model = Keluhan
        fields = '__all__'


class TanggapanForm(AbstractForm):
    class Meta:
        model = Tanggapan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TanggapanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'keluhan':
                self.fields['keluhan'].widget = forms.HiddenInput()
            if field == 'user':
                self.fields['user'].widget = forms.HiddenInput()
