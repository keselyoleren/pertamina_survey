from django import forms

from config.request import get_user

class AbstractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AbstractForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field == 'user' and not get_user().is_superuser:
                self.fields['user'].widget = forms.HiddenInput()