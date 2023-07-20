# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.permisson import IsAuthenticated
from survey.form.pertanyaan_views import QuestionForm

from survey.models import Question, Survey


class QuestionListView(IsAuthenticated, ListView):
    model = Question
    template_name = 'admin-panel/question/list.html'
    context_object_name = 'question_list'

    def get_question(self):
        return Survey.objects.filter(id=self.kwargs['survey_id']).first()

    def get_queryset(self):
        return self.model.objects.filter(survey__id=self.kwargs['survey_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Pertanyaan'
        context['header_title'] = self.get_question().name
        context['create_url'] = reverse_lazy('question-create', kwargs={'survey_id': self.kwargs['survey_id']})
        return context

class QuestionCreateView(CreateView):
    model = Question
    template_name = 'admin-panel/component/form.html'
    form_class = QuestionForm
    success_url = reverse_lazy('question-list')

    def get_question(self):
        return Survey.objects.filter(id=self.kwargs['survey_id']).first()

    def get_success_url(self) -> str:
        return reverse_lazy('question-list', kwargs={'survey_id': self.kwargs['survey_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Pertanyaan'
        context['header_title'] = self.get_question().name
        return context

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'admin-panel/component/form.html'
    form_class = QuestionForm

    def get_question(self):
        return Survey.objects.filter(id=self.kwargs['survey_id']).first()
    
    def get_success_url(self) -> str:
        return reverse_lazy('question-list', kwargs={'survey_id': self.kwargs['survey_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Pertanyaan'
        context['header_title'] = self.get_question().name
        return context

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'admin-panel/component/delete.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('question-list', kwargs={'survey_id': self.kwargs['survey_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Pertanyaan'
        context['header_title'] = 'Delete Pertanyaan'
        return context
