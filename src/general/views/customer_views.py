import json
from django.views.generic import TemplateView
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from config.choice import RoleUser, TypeQuestion
from config.smtp import Smtp
from config.permis import LoginRequiredMixin
from config.survey import MODEL_SURVEY, MODEL_WITH_INTRO
from general.form.informasi_form import InformasiPenerbanganForm
from general.form.keluhan_form import KeluhanForm
from django.contrib import messages
from manage_user.models import AccountUser
from survey.models import Question, Survey
from general.models import Informasi, InformasiPenerbangan, Keluhan, Notification, Tanggapan

class DashboardCustomerView(TemplateView):
    template_name = 'customer/index.html'

class DetailSuerveCustomerView(LoginRequiredMixin, DetailView):
    template_name = 'customer/survey/detail.html'
    model = Survey
    context_object_name = 'survey'

    # def get_template_names(self):
    #     informasi = Informasi.objects.filter(user__ptm_location=self.request.user.ptm_location, \
    #         customer=self.request.user.customer).first()
    #     if informasi:
    #         if informasi.open_survey:
    #             return super().get_template_names()
    #     return 'customer/survey/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_model = []
        # testing
        survey_object = self.get_object()

        # Get all the questions for the given survey
        questions = Question.objects.filter(survey=survey_object).order_by("created_at")

        # Initialize an empty list to store the arrays
        try:
            html_intro = f"<h4>Kepada Yth. <br> <b>Pimpinan {self.request.user.customer}</b> </h4> <b> <p >Suara Anda adalah motivasi kami. Kami ingin mengetahui persepsi Anda tentang Pertamina {self.request.user.ptm_location.location} yang akan kami gunakan untuk menjaga, memperbaiki, dan meningkatkan kinerja kami melayani Anda</p><p ><br>{self.get_object().name}</p></b>"
        except Exception:
            html_intro = f"<h4>Kepada Yth. <br> <b>Pimpinan {self.request.user.customer}</b> </h4> <b> <p >Suara Anda adalah motivasi kami. Kami ingin mengetahui persepsi Anda tentang Pertamina {self.request.user.ptm_location} yang akan kami gunakan untuk menjaga, memperbaiki, dan meningkatkan kinerja kami melayani Anda</p><p ><br>{self.get_object().name}</p></b>"

        arrays = [{
            "name": "page0",
            "elements": [{
                    "type": "html",
                    "name": "question2",
                    "html": html_intro
                    }
                ]
            }
        ]

        # Iterate over the questions and divide them into arrays of maximum size 5
        current_array = []
        for i, question in enumerate(questions, 1):
            if question.type == TypeQuestion.RATING:
                current_array.append(
                    {
                        "type": "rating", 
                        "isRequired": bool(question.is_required),
                        "rateType": "stars",
                        "name": f"{question.slug}",
                        "title": {"default": f"{question.question}",},
                        "rateCount": 10, 
                        "rateMin": 1, 
                        "rateMax": 10, 
                        "minRateDescription": {"default": " Kurang Puas ",},
                        "maxRateDescription": {"default": " Sangat Puas ",}
                    }
                )

            if question.type == TypeQuestion.TEXT:
                current_array.append(
                    {
                        "type": "comment",
                        "name": f"{question.slug}",
                        "title": f"{question.question}",
                        "isRequired": bool(question.is_required),
                    }
                )
            # current_array.append(question)
            # Check if the current array size reaches 5 or it's the last question
            if i % 5 == 0 or i == len(questions):
                arrays.append({
                    "name": f"page{i}",
                    "elements": current_array,
                })
                current_array = []
        # 

        MODEL_WITH_INTRO['pages'] = arrays
        context['model_survey'] = json.dumps(MODEL_WITH_INTRO)
        context['questions'] = Question.objects.filter(survey=self.get_object())
        return context


class SurveyCustomerListView(LoginRequiredMixin, ListView):    
    template_name = 'customer/survey/index.html'
    model = Survey
    context_object_name = 'list_survey'
    

class KeluhanCustomerListView(LoginRequiredMixin, ListView):
    model = Keluhan
    template_name = 'customer/keluhan_list.html'
    context_object_name = 'keluhan_list'
    paginate_by = 10
    object_list = []

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display 5 pages range by default
        # Calculate the current page number and the index of the first page in the range
        current_page = context['page_obj'].number
        first_page_in_range = max(current_page - page_numbers_range, 1)

        # Add the page range to the context
        context['page_range'] = range(first_page_in_range, paginator.num_pages + 1)[:page_numbers_range*2]
        context['header'] = 'Keluhan'
        context['header_title'] = 'List Keluhan'
        return context

class KeluhanCustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Keluhan
    template_name = 'customer/keluhan_detail.html'
    form_class = KeluhanForm
    context_object_name = 'keluhan'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tanggapan'] = Tanggapan.objects.filter(keluhan=self.get_object())
        return context
        


class ReplayKeluhanVIew(LoginRequiredMixin, UpdateView):
    model = Keluhan
    template_name = 'customer/component/form.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-customer-list')
    

class KeluhanCustomerView(LoginRequiredMixin, CreateView):
    model = Keluhan
    template_name = 'customer/keluhan.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-customer-list')

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
        form_valid = super().form_valid(form)
        for user in AccountUser.objects.filter(role_user=RoleUser.DPPU, ptm_location=self.request.user.ptm_location):
            print(user.email)
            notif = Notification.objects.create(
                user=user,
                message = f"Keluhan dari {self.request.user.customer} telah masuk dengan perihal {form.cleaned_data.get('perihal')} ",
                link = reverse('keluhan-detail', kwargs={'pk':self.object.id})
            )   
            
            Smtp(
                template=template,
                subject='Keluhan',
                reciept=[user.email],
                context=context
            ).send_mail()        
        messages.success(self.request, "Keluhan berhasil dikirim")
        return form_valid

class KeluhanCustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Keluhan
    template_name = 'customer/component/delete.html'
    success_url = reverse_lazy('keluhan-customer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Hapus Keluhan'
        return context


class InformasiCustomerView(LoginRequiredMixin, ListView):
    model = Informasi
    template_name = 'customer/informasi.html'
    context_object_name = 'informasi_list'
    paginate_by = 10
    object_list = []

    def get_queryset(self):
        print(self.request.user.customer)
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location, customer=self.request.user.customer).order_by('-created_at')
    
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

class DetailInformasiCreateView(LoginRequiredMixin, DetailView):
    model = Informasi
    template_name = 'customer/detail_informasi.html'
    context_object_name = 'informasi'


class InformasiPenerbanganCustomerView(LoginRequiredMixin, ListView):
    model = InformasiPenerbangan
    template_name = 'customer/informasi_penerbangan.html'
    context_object_name = 'informasi_penerbangan_list'
    paginate_by = 10
    object_list = []

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display 5 pages range by default
        # Calculate the current page number and the index of the first page in the range
        current_page = context['page_obj'].number
        first_page_in_range = max(current_page - page_numbers_range, 1)

        # Add the page range to the context
        context['page_range'] = range(first_page_in_range, paginator.num_pages + 1)[:page_numbers_range*2]
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'List Informasi Penerbangan'
        return context

class DetailInformasiPenerbanganCreateView(LoginRequiredMixin, DetailView):
    model = Informasi
    template_name = 'customer/detail_informasi_penerbangan.html'
    context_object_name = 'informasi_penerbangan'


class CreateInformasiPenerbangan(LoginRequiredMixin, CreateView):
    model = InformasiPenerbangan
    template_name = 'customer/component/form.html'
    form_class = InformasiPenerbanganForm
    success_url = reverse_lazy('informasi-penerbangan-customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = f'Tambah Informasi Penerbangan {self.request.user.customer}'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.maskapai = self.request.user.customer
        messages.success(self.request, "Informasi Penerbangan berhasil ditambahkan")
        return super().form_valid(form)

class UpdateInformasiPenerbangan(LoginRequiredMixin, UpdateView):
    model = InformasiPenerbangan
    template_name = 'customer/component/form.html'
    form_class = InformasiPenerbanganForm
    success_url = reverse_lazy('informasi-penerbangan-customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'Edit Informasi Penerbangan'
        return context

    def form_valid(self, form):
        messages.success(self.request, "Informasi Penerbangan berhasil diubah")
        return super().form_valid(form)

class DeleteInformasiPenerbangan(LoginRequiredMixin, DeleteView):
    model = InformasiPenerbangan
    template_name = 'customer/component/delete.html'
    success_url = reverse_lazy('informasi-penerbangan-customer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'Hapus Informasi Penerbangan'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Informasi Penerbangan berhasil dihapus")
        return super().delete(request, *args, **kwargs)