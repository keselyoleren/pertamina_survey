import json
from django.views import View
from django.views.generic import ListView
from django.http import JsonResponse
from config.permis import LoginRequiredMixin
from manage_user.models import Customer
from survey.models import Question, Responden, SurveyResult

class SaveSurveyView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({'status': 'error'})
        survey_data = request.POST.get('survey_data')
        survey_id = request.POST.get('survey_id')
        responden = Responden.objects.create(user=request.user)

        # Assuming survey_data is a JSON string, parse it to get the required data
        survey_data_json = json.loads(survey_data)
        for key_question, answer in survey_data_json.items():
            question = Question.objects.get(slug=key_question)
            survey_result = SurveyResult()
            survey_result.responden_id=responden.id
            survey_result.customer_id=responden.user.customer.id
            survey_result.question=question
            if type(answer) == int:
                survey_result.resp_int = answer
            elif type(answer) == str:
                survey_result.resp_text = answer
            survey_result.survey_id=int(survey_id)
            survey_result.save()    
            

        return JsonResponse({'status': 'success'})

