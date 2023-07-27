# myapp/views.py

from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from config.choice import RoleUser, TypeQuestion
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
        context['header'] = 'Responden'
        context['header_title'] = 'List Responden'
        return context


class RespondenDetailView(IsAuthenticated, DetailView):
    model = Responden
    template_name = 'admin-panel/responden/view.html'
    context_object_name = 'respondent'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Responden'
        context['numbers'] = list(range(1, 11))
        context['reviews'] = SurveyResult.objects.filter(responden=self.get_object(), question__type=TypeQuestion.RATING)
        context['comments'] = SurveyResult.objects.filter(responden=self.get_object(), question__type=TypeQuestion.TEXT)
        context['header_title'] = f'Survey oleh {self.get_object().user.username} Customer dari {self.get_object().user.customer.name}' 
        return context


class RespondenDeleteView(DeleteView):
    model = Responden
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('survey-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = 'Delete Survey'
        return context


class TotalSurveyView(IsAuthenticated, ListView):
    model = Customer
    template_name = 'admin-panel/responden/total.html'
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = f'TotalHasil Survey customer  {self.request.user.ptm_location}'
        context['questions'] = Question.objects.filter(type=TypeQuestion.RATING)
        return context
    