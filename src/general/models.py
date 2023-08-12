from django.db import models
from django.utils.translation import gettext as _
from config.choice import PerihalKeluhan, PrihalInformasi
from config.models import BaseModel
from config.request import get_user
from manage_user.models import AccountUser, Customer




# Create your models here.
class Keluhan(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    perihal = models.CharField(_("Perihal"), max_length=255, choices=PerihalKeluhan.choices)
    komentar = models.TextField(_("Komentar"))

    def __str__(self) -> str:
        return self.perihal
    
    def save(self, *args, **kwargs):
        if not get_user().is_superuser:
            self.customer = get_user().customer
            self.user = get_user()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Keluhan")
        verbose_name_plural = _("Keluhan")

class Informasi(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    perihal = models.CharField(_("Perihal"), max_length=255, choices=PrihalInformasi.choices)
    informasi = models.TextField(_("Informasi"))


    def __str__(self) -> str:
        return self.user.username

    def save(self, *args, **kwargs):
        if not get_user().is_superuser:
            self.user = get_user()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Informasi")
        verbose_name_plural = _("Informasi")

class InformasiPenerbangan(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    waktu = models.DateTimeField(_("Waktu"), blank=True, null=True)
    tujuan = models.CharField(_("Tujuan"), max_length=255, blank=True, null=True)
    maskapai = models.ForeignKey(Customer, on_delete=models.CASCADE)
    penerbangan = models.CharField(_("Penerbangan"), max_length=255, blank=True, null=True)
    terminal = models.CharField(_("Terminal"), max_length=255, blank=True, null=True)
    keterangan = models.CharField(_("Keterangan"), max_length=255, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        self.user = get_user()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.tujuan} - {self.penerbangan}"   

    class Meta:
        verbose_name = _("Informasi Penerbangan")
        verbose_name_plural = _("Informasi Penerbangan")

        