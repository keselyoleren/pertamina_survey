from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from config.choice import RoleUser
from config.models import BaseModel

# Create your models here.
class PTM(BaseModel):
    location = models.CharField(_("PTM Location"), max_length=100)

    def __str__(self) -> str:
        return self.location

    class Meta:
        verbose_name = _("PTM Location")
        verbose_name_plural = _("PTM Location")

class Instansi(BaseModel):
    name = models.CharField(_("Nama Instansi"), max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Instansi")
        verbose_name_plural = _("Instansi")


class Customer(BaseModel):
    cus_id = models.CharField(_("Customer ID"), max_length=100, unique=True)
    name = models.CharField(_("Nama Customer"), max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customer")


class AccountUser(AbstractUser):
    ptm_location = models.ForeignKey(PTM, on_delete=models.CASCADE, null=True, blank=True)
    role_user = models.CharField(_("Role User"), max_length=20, choices=RoleUser.choices, default=RoleUser.CUSTOMNER)
    jabatan = models.CharField(_("Jabatan"), max_length=100, null=True, blank=True)
    instansi = models.CharField(_("Instansi"), max_length=100, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, help_text="jika role user adalah superadmin dan dppu maka field ini tidak usah di isi")