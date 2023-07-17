from django.db.models import TextChoices

class RoleUser(TextChoices):
    SUPER_ADMIN = 'super admin'
    DPPU = 'dppu'
    CUSTOMNER = 'customer'

class TypeQuestion(TextChoices):
    INT = 'integer'
    TEXT = 'text'
    COICES = 'choices'

    