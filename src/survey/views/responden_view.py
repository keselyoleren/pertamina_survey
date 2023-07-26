# myapp/views.py

from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from config.choice import TypeQuestion
from config.permis import IsAuthenticated

from survey.models import Survey, Responden, SurveyResult
from survey.form.suervey_form import SurveyForm

class RespondenListView(IsAuthenticated, ListView):
    model = Responden
    template_name = 'admin-panel/responden/list.html'
    context_object_name = 'respondents'
    
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
