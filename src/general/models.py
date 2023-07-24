from operator import mod
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
from config.models import BaseModel
from config.request import get_user
from manage_user.models import AccountUser, Customer
from ckeditor.fields import RichTextField



# Create your models here.
class Keluhan(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    perihal = models.CharField(_("Perihal"), max_length=255)
    komentar = RichTextField(_("Komentar"))

    def __str__(self) -> str:
        return self.perihal
    
    def save(self, *args, **kwargs):
        if not get_user().is_superuser:
            self.user = get_user()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Keluhan")
        verbose_name_plural = _("Keluhan")

class Informasi(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    informasi = RichTextField(_("Informasi"))

    def __str__(self) -> str:
        return self.user.username

    def save(self, *args, **kwargs):
        if not get_user().is_superuser:
            self.user = get_user()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Informasi")
        verbose_name_plural = _("Informasi")
