
from config.form import AbstractForm
from manage_user.models import Instansi

class InstansiForm(AbstractForm):
    class Meta:
        model = Instansi
        fields = '__all__'