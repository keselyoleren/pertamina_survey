from django.contrib import admin

from survey.models import Question, Responden, Survey

# Register your models here.
@admin.register(Survey)
class SurveyAdminView(admin.ModelAdmin):
    list_display = ('id','name','description')

@admin.register(Question)
class QuestionAdminView(admin.ModelAdmin):
    list_display = ('id','question','type')

@admin.register(Responden)
class RespondenAdminView(admin.ModelAdmin):
    list_display = ('id','user','custumer','question')
