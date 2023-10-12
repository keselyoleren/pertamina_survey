# myapp/views.py

import datetime
from django.views.generic import ListView, DetailView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from config.choice import RoleUser, TypeQuestion
from config.export import GeneratePDF
from config.permis import IsAuthenticated
from manage_user.models import Customer

from survey.models import Question, Survey, Responden, SurveyResult
from survey.form.suervey_form import SurveyForm

class RespondenListView(IsAuthenticated, ListView):
    model = Responden
    template_name = 'admin-panel/responden/list.html'
    context_object_name = 'respondents'
    
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset()
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Hasil Survey'
        context['header_title'] = 'List Hasil Survey'
        return context


class RespondenDetailView(IsAuthenticated, DetailView, GeneratePDF):
    model = Responden
    template_name = 'admin-panel/responden/view.html'
    context_object_name = 'respondent'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Responden'
        context['numbers'] = list(range(1, 11))
        context['reviews'] = SurveyResult.objects.filter(responden=self.get_object(), question__type=TypeQuestion.RATING).order_by('created_at')
        context['comments'] = SurveyResult.objects.filter(responden=self.get_object(), question__type=TypeQuestion.TEXT)
        context['header_title'] = f'Customer {self.get_object().user.customer.name}' 
        return context

class ExportRespondenDetailView(IsAuthenticated, DetailView, GeneratePDF):
    model = Responden
    template_name = 'admin-panel/export/survey_result.html'
    context_object_name = 'respondent'

    def get(self, request, *args, **kwargs):
        context = {}
        context['numbers'] = list(range(1, 11))
        context['reviews'] = SurveyResult.objects.filter(responden=self.get_object(), question__type=TypeQuestion.RATING)
        context['comments'] = SurveyResult.objects.filter(responden=self.get_object(), question__type=TypeQuestion.TEXT)
        context['header_title'] = f'Customer {self.get_object().user.customer.name}' 
        context['customer'] = self.get_object().user.customer.name
        context['ptm'] = self.get_object().user.ptm_location
        context['created_at'] = self.get_object().created_at

        return self.render_to_pdf(
            context, 
            self.template_name,
            '/css/pdf/export.css', 
            'survey_result.pdf'
        )


class RespondenDeleteView(DeleteView):
    model = Responden
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('responden-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = 'Delete Hasil Survey'
        return context


class TotalSurveyView(IsAuthenticated, ListView):
    model = Customer
    template_name = 'admin-panel/responden/total.html'
    context_object_name = 'customers'

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset()
        return super().get_queryset().filter(lokasi=self.request.user.ptm_location)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = f'Total Survey  {self.request.user.ptm_location}'
        context['questions'] = Question.objects.filter(type=TypeQuestion.RATING)
        # context['comments'] = SurveyResult.objects.filter(question__type=TypeQuestion.TEXT)
        context['customer'] = self.request.user.customer
        context['ptm'] = self.request.user.ptm_location
        context['created_at'] = datetime.datetime.now()
        return context
    

class ExportTotalSurveyView(IsAuthenticated, ListView, GeneratePDF):
    model = Customer
    template_name = 'admin-panel/export/total_survey_result.html'
    context_object_name = 'customers'

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset()
        return super().get_queryset().filter(lokasi=self.request.user.ptm_location)

    def get(self, request, *args, **kwargs):
        context = {}
        context['header'] = 'Survey'
        context['header_title'] = f'Total Survey  {self.request.user.ptm_location}'
        context['customer'] = self.request.user.customer
        context['ptm'] = self.request.user.ptm_location
        context['created_at'] = datetime.datetime.now()
        context['questions'] = Question.objects.filter(type=TypeQuestion.RATING)
        return self.render_to_pdf(
            context, 
            self.template_name,
            '/css/pdf/export.css', 
            f'total_survey_{self.request.user.ptm_location}.pdf'
        )
