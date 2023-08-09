# myapp/views.py


import contextlib
from audioop import avg
from config.choice import RoleUser, TypeQuestion
from config.permis import IsAuthenticated

from django.views.generic import TemplateView
from django.db.models import Avg, Min, Max, F
from general.models import Keluhan

from manage_user.models import Customer
from survey.models import Question, Responden, Survey, SurveyResult


class DashboardView(IsAuthenticated, TemplateView):
    template_name = 'admin-panel/index.html'

    def get_context_data(self, **kwargs):
        average_results = SurveyResult.objects.filter(
            responden__user__ptm_location=self.request.user.ptm_location, question__type=TypeQuestion.RATING
        ).aggregate(
            avg_resp_int=Avg('resp_int'),
            min_resp_int=Min('resp_int'),
            max_resp_int=Max('resp_int')
        )

        min_max_result = SurveyResult.objects.filter(
            responden__user__ptm_location=self.request.user.ptm_location, question__type=TypeQuestion.RATING
        ).annotate(min_resp_int=Min('resp_int'), max_resp_int=Max('resp_int'), avg_resp_int=Avg('resp_int'))    


        survey = Survey.objects.first()
        question = Question.objects.filter(survey=survey, type=TypeQuestion.RATING)
        label = []
        scores = []
        for q in question:
            label.append(q.question)
            average_result = SurveyResult.objects.filter(question__id=q.id, responden__user__ptm_location=self.request.user.ptm_location).aggregate(
                avg_resp_int=Avg('resp_int'))
            scores.append(average_result['avg_resp_int'])

        keluhan = Keluhan.objects.filter(user__ptm_location=self.request.user.ptm_location).last()
        responden = Responden.objects.filter(user__ptm_location=self.request.user.ptm_location).last()
        total_survey = SurveyResult.objects.filter(customer__lokasi=self.request.user.ptm_location).count()
        total_customer = Customer.objects.filter(lokasi=self.request.user.ptm_location).count()

        if self.request.user.is_superuser or self.request.user.role_user == RoleUser.SUPER_ADMIN:
            average_result = SurveyResult.objects.filter(question__type=TypeQuestion.RATING).aggregate(
                avg_resp_int=Avg('resp_int'),
                min_resp_int=Min('resp_int'),
                max_resp_int=Max('resp_int')
            )

            min_max_result = SurveyResult.objects.filter(question__type=TypeQuestion.RATING
            ).annotate(min_resp_int=Min('resp_int'), max_resp_int=Max('resp_int'), avg_resp_int=Avg('resp_int'))    


            survey = Survey.objects.first()
            question = Question.objects.filter(survey=survey, type=TypeQuestion.RATING)
            label = []
            scores = []
            for q in question:
                label.append(q.question)
                average_result = SurveyResult.objects.filter(question__id=q.id).aggregate(
                    avg_resp_int=Avg('resp_int'))
                scores.append(average_result['avg_resp_int'])

            keluhan = Keluhan.objects.last()
            responden = Responden.objects.last()
            total_survey = SurveyResult.objects.count()
            total_customer = Customer.objects.count()


        context =  super().get_context_data(**kwargs)
        context['customers'] = total_customer
        context['top_rating'] = average_results['max_resp_int']
        context['low_rating'] = average_results['min_resp_int']
        context['survey_received'] = total_survey
        context['questions'] = label
        context['scores'] = scores
        context['keluhan'] = keluhan
        context['responden'] = responden
        with contextlib.suppress(Exception):
            context['top_survey'] = min_max_result.order_by('-avg_resp_int').first().question.question
            context['low_survey'] = min_max_result.order_by('avg_resp_int').first().question.question
        return context