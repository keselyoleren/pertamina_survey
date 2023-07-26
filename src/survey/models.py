from django.db import models
from config.choice import TypeQuestion
from config.models import BaseModel
from django.utils.translation import gettext as _
from django.utils.text import slugify
from config.request import get_user

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
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=True, null=True)
    question = models.CharField(_("Pertanyaan"), max_length=255)
    is_required = models.BooleanField(_("Wajib diisi"), default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    type = models.CharField(_("Tipe Pertanyaan"), max_length=255, choices=TypeQuestion.choices)

    def __str__(self) -> str:
        return self.question


    def save(self, *args, **kwargs):
        slug_field = f"{self.pk} {self.question}"
        self.slug = slugify(slug_field)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Pertanyaan")
        verbose_name_plural = _("Pertanyaan")

class Responden(BaseModel):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class SurveyResult(BaseModel):
    responden = models.ForeignKey(Responden, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    resp_int = models.CharField(_("Respon nilai"), max_length=100,  blank=True, null=True)
    resp_text = models.TextField(_("Respon Text"), blank=True, null=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    
    def __str__(self) -> str:
        return f"{self.responden.user.username} {self.customer.name}"
    
    
    class Meta:
        verbose_name = _("Survey Result")
        verbose_name_plural = _("Survey Result")