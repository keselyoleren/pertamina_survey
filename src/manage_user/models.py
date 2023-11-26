import contextlib
from operator import mod
import profile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from config.choice import RoleUser
from config.models import BaseModel

from PIL import Image

# Create your models here.
class PTM(BaseModel):
    lokasi_id = models.CharField(_("Lokasi ID"), max_length=100, unique=True)
    location = models.CharField(_("Lokasi"), max_length=100)

    def __str__(self) -> str:
        with contextlib.suppress(Exception):
            return f"{self.lokasi_id} - {self.location}"

    class Meta:
        verbose_name = _("Lokasi DPPU")
        verbose_name_plural = _("Lokasi DPPU")

class Instansi(BaseModel):
    name = models.CharField(_("Nama Instansi"), max_length=100)

    def __str__(self) -> str:
        with contextlib.suppress(Exception):
            return self.name
    
    class Meta:
        verbose_name = _("Instansi")
        verbose_name_plural = _("Instansi")


class Customer(BaseModel):
    cus_id = models.CharField(_("Customer ID"), max_length=100, unique=True)
    lokasi = models.ForeignKey(PTM, on_delete=models.CASCADE, verbose_name=_("Lokasi"))
    name = models.CharField(_("Nama Customer"), max_length=100)
    
    def __str__(self) -> str:
        with contextlib.suppress(Exception):
            return f"{self.cus_id} - {self.name} "
    
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customer")


class AccountUser(AbstractUser):
    profile_picture = models.ImageField(_("Profile Picture"), upload_to='profile_picture/', null=True, blank=True, default='profile_picture/default.png')
    ptm_location = models.ForeignKey(PTM, on_delete=models.CASCADE, null=True, blank=True,verbose_name=_("Lokasi"))
    role_user = models.CharField(_("Role User"), max_length=20, choices=RoleUser.choices, default=RoleUser.CUSTOMER)
    jabatan = models.CharField(_("Jabatan"), max_length=100, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Customer ID"))
    login_attempts = models.IntegerField(default=0)
    is_locked = models.BooleanField(default=False)



    def save(self, *args, **kwargs):
        with contextlib.suppress(Exception):
            img = Image.open(self.profile_picture)
            if img.height > 200 or img.width > 200:
                output_size = (200,200)
                img.thumbnail(output_size)
                img.save(self.profile_picture)
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
        
    