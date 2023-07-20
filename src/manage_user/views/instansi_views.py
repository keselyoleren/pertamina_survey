# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.permisson import IsAuthenticated
from manage_user.form.instansi_form import InstansiForm
from manage_user.models import Instansi

class InstansiListView(IsAuthenticated, ListView):
    model = Instansi
    template_name = 'admin-panel/instansi/list.html'
    context_object_name = 'instansi_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Instansi'
        context['header_title'] = 'List Instansi'
        context['create_url'] = reverse_lazy('instansi-create')
        return context

class InstansiCreateView(CreateView):
    model = Instansi
    template_name = 'admin-panel/component/form.html'
    form_class = InstansiForm
    success_url = reverse_lazy('instansi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Instansi'
        context['header_title'] = 'Tambah Instansi'
        return context

class InstansiUpdateView(UpdateView):
    model = Instansi
    template_name = 'admin-panel/component/form.html'
    form_class = InstansiForm
    success_url = reverse_lazy('instansi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Instansi'
        context['header_title'] = 'Edit instansi'
        return context

class InstansiDeleteView(DeleteView):
    model = Instansi
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('instansi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Instansi'
        context['header_title'] = 'Delete Instansi'
        return context
