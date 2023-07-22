from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from general.form.keluhan_form import KeluhanForm

from general.models import Keluhan

class DashboardCustomerView(TemplateView):
    template_name = 'customer/index.html'

class SuerveCustomerView(TemplateView):
    template_name = 'customer/survey.html'

class KeluhanCustomerView(CreateView):
    model = Keluhan
    template_name = 'customer/keluhan.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Tambah Keluhan'
        return context

class InformasiCustomerView(TemplateView):
    template_name = 'customer/informasi.html'