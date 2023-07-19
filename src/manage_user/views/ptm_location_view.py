# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from manage_user.form.ptm_location_form import PTMForm
from manage_user.models import PTM

class PTMListView(ListView):
    model = PTM
    template_name = 'admin-panel/ptm_location/list.html'
    context_object_name = 'location_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'PTM'
        context['header_title'] = 'List lokasi PTM'
        context['create_url'] = reverse_lazy('ptm-create')
        return context

class PTMCreateView(CreateView):
    model = PTM
    template_name = 'admin-panel/component/form.html'
    form_class = PTMForm
    success_url = reverse_lazy('ptm-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'lokasi PTM'
        context['header_title'] = 'Tambah lokasi PTM'
        return context

class PTMUpdateView(UpdateView):
    model = PTM
    template_name = 'admin-panel/component/form.html'
    form_class = PTMForm
    success_url = reverse_lazy('ptm-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Lokasi PTM'
        context['header_title'] = 'Edit lokasi PTM'
        return context

class PTMDeleteView(DeleteView):
    model = PTM
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('ptm-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Lokasi PTM'
        context['header_title'] = 'Delete Lokasi PTM'
        return context
