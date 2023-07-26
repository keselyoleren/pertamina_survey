from django.db.models import TextChoices

class RoleUser(TextChoices):
    SUPER_ADMIN = 'super admin'
    DPPU = 'dppu'
    CUSTOMNER = 'customer'

class TypeQuestion(TextChoices):
    RATING = 'rating'
    TEXT = 'text'
    

    