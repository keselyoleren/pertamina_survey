# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.permisson import IsAuthenticated

from survey.models import Survey
from survey.form.suervey_form import SurveyForm

class SurveyListView(IsAuthenticated, ListView):
    model = Survey
    template_name = 'admin-panel/survey/list.html'
    context_object_name = 'survey_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = 'List Survey'
        context['create_url'] = reverse_lazy('survey-create')
        return context

class SurveyCreateView(CreateView):
    model = Survey
    template_name = 'admin-panel/component/form.html'
    form_class = SurveyForm
    success_url = reverse_lazy('survey-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = 'Tambah Survey'
        return context

class SurveyUpdateView(UpdateView):
    model = Survey
    template_name = 'admin-panel/component/form.html'
    form_class = SurveyForm
    success_url = reverse_lazy('survey-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = 'Edit Survey'
        return context

class SurveyDeleteView(DeleteView):
    model = Survey
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('survey-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Survey'
        context['header_title'] = 'Delete Survey'
        return context
