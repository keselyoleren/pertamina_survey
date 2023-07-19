# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from general.form.informasi_form import InformasiForm

from general.models import Informasi

class InformasiListView(ListView):
    model = Informasi
    template_name = 'admin/informasi/list.html'
    context_object_name = 'informasi_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'List Informasi'
        context['create_url'] = reverse_lazy('informasi-create')
        return context

class InformasiCreateView(CreateView):
    model = Informasi
    template_name = 'admin/component/form.html'
    form_class = InformasiForm
    success_url = reverse_lazy('informasi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'Tambah Informasi'
        return context

class InformasiUpdateView(UpdateView):
    model = Informasi
    template_name = 'admin/component/form.html'
    form_class = InformasiForm
    success_url = reverse_lazy('informasi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'Edit Informasi'
        return context

class InformasiDeleteView(DeleteView):
    model = Informasi
    template_name = 'admin/component/delete.html'
    success_url = reverse_lazy('informasi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'Delete Informasi'
        return context
