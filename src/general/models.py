from operator import mod
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
from config.models import BaseModel
from manage_user.models import AccountUser, Customer


# Create your models here.
class Keluhan(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    perihal = models.CharField(_("Perihal"), max_length=255)
    komentar = models.TextField(_("Komentar"))

    def __str__(self) -> str:
        return self.perihal
    
    class Meta:
        verbose_name = _("Keluhan")
        verbose_name_plural = _("Keluhan")

class Informasi(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Informasi = models.TextField(_("Komentar"))

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        verbose_name = _("Informasi")
        verbose_name_plural = _("Informasi")
