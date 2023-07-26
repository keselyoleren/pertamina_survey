import json
from django.views import View
from django.http import JsonResponse
from survey.models import Responden

class SaveSurveyView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            survey_data = request.POST.get('survey_data')
            survey_id = request.POST.get('survey_id')
            # Assuming survey_data is a JSON string, parse it to get the required data
            survey_data_json = json.loads(survey_data)
            for question, answer in survey_data_json.items():
                
                print('question: ', question)
                print('answer: ', type(answer))


            print(survey_data_json)

            return JsonResponse({'status': 'success'})

        return JsonResponse({'status': 'error'})
