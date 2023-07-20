
from config.form import AbstractForm
from survey.models import Survey

class SurveyForm(AbstractForm):
    class Meta:
        model = Survey
        fields = '__all__'