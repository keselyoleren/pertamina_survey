from django.contrib import admin

from general.models import Informasi, Keluhan

# Register your models here.
@admin.register(Keluhan)
class KeluhanAdminView(admin.ModelAdmin):
    list_display = ('id','user','custumer','perihal','komentar')

@admin.register(Informasi)
class InformasiAdminView(admin.ModelAdmin):
    list_display = ('id','user','customer','informasi')
    