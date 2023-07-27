
from django import template
from config.choice import RoleUser
from survey.models import SurveyResult
from django.db.models import Avg
from config.request import get_user
register = template.Library()

@register.filter(name='survey_result')
def survey_result(question, customer):
    average_result = SurveyResult.objects.filter(question_id=question, customer_id=customer, responden__user__ptm_location=get_user().ptm_location).aggregate(avg_resp_int=Avg('resp_int'))
    if get_user().is_superuser or get_user().role_user == RoleUser.SUPER_ADMIN:
        average_result = SurveyResult.objects.filter(question_id=question, customer_id=customer).aggregate(avg_resp_int=Avg('resp_int'))
    return average_result['avg_resp_int']
    # return question.survey_result(responden)