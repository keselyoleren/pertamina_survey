# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.choice import RoleUser
from config.permis import IsAuthenticated, LoginRequiredMixin
from general.form.informasi_form import InformasiForm

from general.models import Informasi

class InformasiListView(IsAuthenticated, ListView):
    model = Informasi
    template_name = 'admin-panel/informasi/list.html'
    context_object_name = 'informasi_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset()
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'List Informasi'
        context['create_url'] = reverse_lazy('informasi-create')
        return context

class InformasiCreateView(IsAuthenticated, CreateView):
    model = Informasi
    template_name = 'admin-panel/component/form.html'
    form_class = InformasiForm
    success_url = reverse_lazy('informasi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'Tambah Informasi'
        return context

class InformasiUpdateView(IsAuthenticated, UpdateView):
    model = Informasi
    template_name = 'admin-panel/component/form.html'
    form_class = InformasiForm
    success_url = reverse_lazy('informasi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'Edit Informasi'
        return context

class InformasiDeleteView(IsAuthenticated, DeleteView):
    model = Informasi
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('informasi-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'Delete Informasi'
        return context
