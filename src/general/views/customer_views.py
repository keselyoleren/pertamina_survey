import json
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from config.choice import RoleUser, TypeQuestion
from config.smtp import Smtp
from config.permis import LoginRequiredMixin
from config.survey import MODEL_SURVEY
from general.form.keluhan_form import KeluhanForm
from django.contrib import messages
from manage_user.models import AccountUser
from survey.models import Question, Survey
from general.models import Informasi, Keluhan

class DashboardCustomerView(TemplateView):
    template_name = 'customer/index.html'

class DetailSuerveCustomerView(LoginRequiredMixin, DetailView):
    template_name = 'customer/survey/detail.html'
    model = Survey
    context_object_name = 'survey'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_model = []
        for data in Question.objects.filter(survey=self.get_object()):
            if data.type == TypeQuestion.RATING:
                data_model.append(
                    {
                        "type": "rating", 
                        "isRequired": bool(data.is_required),
                        "name": f"{data.slug}",
                        "title": {"default": f"{data.question}",},
                        "rateCount": 10, 
                        "rateMin": 0, 
                        "rateMax": 9, 
                        "minRateDescription": {"default": "Tidak Suka",},
                        "maxRateDescription": {"default": "Sangat Suka",}
                    }
                )

            if data.type == TypeQuestion.TEXT:
                data_model.append(
                    {
                        "type": "comment",
                        "name": f"{data.slug}",
                        "title": f"{data.question}",
                        "isRequired": bool(data.is_required),
                    }
                )
        MODEL_SURVEY['title'] = self.get_object().name
        MODEL_SURVEY['pages'][0]['elements'][0]['elements'] = data_model
        context['model_survey'] = json.dumps(MODEL_SURVEY)
        context['questions'] = Question.objects.filter(survey=self.get_object())
        return context


class SurveyCustomerListView(LoginRequiredMixin, ListView):    
    template_name = 'customer/survey/index.html'
    model = Survey
    context_object_name = 'list_survey'
    

class KeluhanCustomerView(CreateView):
    model = Keluhan
    template_name = 'customer/keluhan.html'
    form_class = KeluhanForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Tambah Keluhan'
        return context

    def form_valid(self, form):
        template = 'email/keluhan.html'
        context = {
            'user':self.request.user,
            'perihal':form.cleaned_data.get('perihal'),
            'komentar':form.cleaned_data.get('komentar'),
        }
        for user in AccountUser.objects.filter(role_user=RoleUser.DPPU, ptm_location=self.request.user.ptm_location):
            Smtp(
                template=template,
                subject='Keluhan',
                reciept=[user.email],
                context=context
            ).send_mail()        
        messages.success(self.request, "Keluhan berhasil dikirim")
        return super().form_valid(form)


class InformasiCustomerView(ListView):
    model = Informasi
    template_name = 'customer/informasi.html'
    context_object_name = 'informasi_list'
    paginate_by = 10
    object_list = []

    def get_queryset(self):
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display 5 pages range by default
        # Calculate the current page number and the index of the first page in the range
        current_page = context['page_obj'].number
        first_page_in_range = max(current_page - page_numbers_range, 1)

        # Add the page range to the context
        context['page_range'] = range(first_page_in_range, paginator.num_pages + 1)[:page_numbers_range*2]
        context['header'] = 'Informasi'
        context['header_title'] = 'List Informasi'
        return context

class DetailInformasiCreateView(DetailView):
    model = Informasi
    template_name = 'customer/detail_informasi.html'
    context_object_name = 'informasi'
