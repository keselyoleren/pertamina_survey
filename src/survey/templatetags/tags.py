
from django import template
from config.choice import RoleUser
from survey.models import Survey, SurveyResult
from django.db.models import Avg
from config.request import get_user
register = template.Library()

@register.filter(name='survey_result')
def survey_result(question, customer):
    try:
        average_result = SurveyResult.objects.filter(question_id=question, customer_id=customer, responden__user__ptm_location=get_user().ptm_location).aggregate(avg_resp_int=Avg('resp_int'))
        if get_user().is_superuser or get_user().role_user == RoleUser.SUPER_ADMIN:
            average_result = SurveyResult.objects.filter(question_id=question, customer_id=customer).aggregate(avg_resp_int=Avg('resp_int'))
        return "{:.1f}".format(average_result['avg_resp_int'])
    except Exception:
        return "-"

    # return question.survey_result(responden)

@register.filter(name='avg_survey')
def avg_survey(question):
    average_result = SurveyResult.objects.filter(question_id=question, responden__user__ptm_location=get_user().ptm_location).aggregate(avg_resp_int=Avg('resp_int'))
    return "{:.1f}".format(average_result['avg_resp_int'])
    


@register.filter(name='get_survey')
def get_survey(arg):
    return Survey.objects.all().first().id

@register.filter
def format_size(value):
    kb_size = value / 1024
    if kb_size < 1024:
        return f"{kb_size:.2f} KB"
    mb_size = kb_size / 1024
    if mb_size < 1024:
        return f"{mb_size:.2f} MB"
    gb_size = mb_size / 1024
    return f"{gb_size:.2f} GB"