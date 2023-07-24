from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from config.permis import LoginRequiredMixin
from general.form.keluhan_form import KeluhanForm
from django.contrib import messages

from general.models import Informasi, Keluhan

class DashboardCustomerView(TemplateView):
    template_name = 'customer/index.html'

class SuerveCustomerView(TemplateView):
    template_name = 'customer/survey.html'

class KeluhanCustomerView(LoginRequiredMixin, CreateView):
    model = Keluhan
    template_name = 'customer/keluhan.html'
    form_class = KeluhanForm
    success_url = '/keluhan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Tambah Keluhan'
        return context

    def form_valid(self, form):
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
