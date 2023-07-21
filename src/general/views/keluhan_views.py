# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.permis import IsAuthenticated
from config.choice import RoleUser
from general.form.keluhan_form import KeluhanForm

from general.models import Keluhan



class KeluhanListView(IsAuthenticated, ListView):
    model = Keluhan
    template_name = 'admin-panel/keluhan/list.html'
    context_object_name = 'keluhan_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset()
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'List Keluhan'
        context['create_url'] = reverse_lazy('keluhan-create')
        return context

class KeluhanCreateView(CreateView):
    model = Keluhan
    template_name = 'admin-panel/component/form.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Tambah Keluhan'
        return context

class KeluhanUpdateView(UpdateView):
    model = Keluhan
    template_name = 'admin-panel/component/form.html'
    form_class = KeluhanForm
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Edit Keluhan'
        return context

class KeluhanDeleteView(DeleteView):
    model = Keluhan
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['header_title'] = 'Delete Keluhan'
        return context
