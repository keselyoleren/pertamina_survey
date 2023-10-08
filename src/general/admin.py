from django.contrib import admin

from general.models import Informasi, Keluhan, Notification

# Register your models here.
@admin.register(Keluhan)
class KeluhanAdminView(admin.ModelAdmin):
    list_display = ('id','user','customer','perihal','komentar')

@admin.register(Informasi)
class InformasiAdminView(admin.ModelAdmin):
    list_display = ('id','user','customer','informasi')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list    = ('id','user','message', 'link')
    