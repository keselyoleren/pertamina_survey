from tabnanny import verbose
from django.db import models
from config.choice import TypeQuestion
from config.models import BaseModel
from django.utils.translation import gettext as _

from manage_user.models import AccountUser, Customer

# Create your models here.
class Survey(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Survey")
        verbose_name_plural = _("Survey")

class Question(BaseModel):
    question = models.CharField(_("Pertanyaan"), max_length=255)
    type = models.CharField(_("Tipe Pertanyaan"), max_length=255, choices=TypeQuestion.choices)
    
    class Meta:
        verbose_name = _("Pertanyaan")
        verbose_name_plural = _("Pertanyaan")

class Responden(BaseModel):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]

    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    resp_int = models.CharField(_("Respon nilai"), max_length=255, choices=RATING_CHOICES, blank=True, null=True)
    resp_text = models.TextField(_("Respon Text"), blank=True, null=True)

    
    def __str__(self) -> str:
        return f"{self.user.username} {self.custumer.name}"
    
    
    class Meta:
        verbose_name = _("Responden")
        verbose_name_plural = _("Responden")