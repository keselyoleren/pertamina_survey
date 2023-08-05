from webbrowser import get
from django import forms

from config.request import get_user

class AbstractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AbstractForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'survey':
                self.fields['survey'].widget = forms.HiddenInput()
            if field == 'slug':
                self.fields['slug'].widget = forms.HiddenInput()

            if not get_user().is_superuser and field == 'customer':
                self.fields['customer'].widget = forms.HiddenInput()

            if field != 'is_required':
                self.fields[field].widget.attrs['class'] = 'form-control'
                if field == 'user' and not get_user().is_superuser:
                    self.fields['user'].widget = forms.HiddenInput()

            if not get_user().is_superuser and field == 'ptm_location':
                self.fields['ptm_location'].widget.attrs['disabled'] = 'disabled'

            if not get_user().is_superuser and field == 'jabatan':
                self.fields['jabatan'].widget.attrs['disabled'] = 'disabled'