from django.contrib import admin

from survey.models import Question, Responden, SurveyResult, Survey

# Register your models here.
@admin.register(Survey)
class SurveyAdminView(admin.ModelAdmin):
    list_display = ('id','name','description')

@admin.register(Question)
class QuestionAdminView(admin.ModelAdmin):
    list_display = ('id','question','type')

@admin.register(Responden)
class RespondenAdminView(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(SurveyResult)
class SurveyResultAdminView(admin.ModelAdmin):
    list_display = ('id','responden', 'customer','question', 'resp_int', 'resp_text')
