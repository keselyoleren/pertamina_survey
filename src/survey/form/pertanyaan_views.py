
from config.form import AbstractForm
from survey.models import Question, Survey

class QuestionForm(AbstractForm):
    class Meta:
        model = Question
        fields = '__all__'