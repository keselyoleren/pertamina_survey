from django.db.models import TextChoices

class RoleUser(TextChoices):
    SUPER_ADMIN = 'super admin'
    DPPU = 'dppu'
    CUSTOMER = 'customer'

class TypeQuestion(TextChoices):
    RATING = 'rating'
    TEXT = 'text'
    

    