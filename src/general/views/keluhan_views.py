# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from general.form.keluhan_form import KeluhanForm

from general.models import Keluhan


class KeluhanListView(ListView):
    model = Keluhan
    template_name = 'admin/keluhan/list.html'
    context_object_name = 'keluhan_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'List Keluhan'
        context['create_url'] = reverse_lazy('keluhan-create')
        return context

class KeluhanCreateView(CreateView):
    model = Keluhan
    template_name = 'admin/component/form.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Tambah Keluhan'
        return context

class KeluhanUpdateView(UpdateView):
    model = Keluhan
    template_name = 'admin/component/form.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Edit Keluhan'
        return context

class KeluhanDeleteView(DeleteView):
    model = Keluhan
    template_name = 'admin/component/delete.html'
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Delete Keluhan'
        return context
