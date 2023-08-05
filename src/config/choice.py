from django.db.models import TextChoices

class RoleUser(TextChoices):
    SUPER_ADMIN = 'super admin'
    DPPU = 'dppu'
    CUSTOMER = 'customer'

class TypeQuestion(TextChoices):
    RATING = 'rating'
    TEXT = 'text'
    

class PrihalInformasi(TextChoices):
    DISTRIBUSI = 'Distribusi'
    SURVEY = 'Survey'

class PerihalKeluhan(TextChoices):
    DELAY = 'Delay'
    QUALITY_PRODUCT = 'Quality Product'
    HOSPITALITY = 'Hospitality'
    OTHER = 'Other'