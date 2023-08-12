# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.choice import RoleUser
from config.permis import IsAuthenticated, LoginRequiredMixin
from general.form.informasi_form import InformasiPenerbanganForm


from general.models import InformasiPenerbangan

class InformasiPenerbanganListView(IsAuthenticated, ListView):
    model = InformasiPenerbangan
    template_name = 'admin-panel/informasi_penerbangan/list.html'
    context_object_name = 'informasi_penerbangan'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset()
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'List Informasi Penerbangan'
        context['create_url'] = reverse_lazy('informasi_penerbangan-create')
        return context

class InformasiPenerbanganCreateView(IsAuthenticated, CreateView):
    model = InformasiPenerbangan
    template_name = 'admin-panel/component/form.html'
    form_class = InformasiPenerbanganForm
    success_url = reverse_lazy('informasi_penerbangan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'Tambah Informasi Penerbangan'
        return context

class InformasiPenerbanganUpdateView(IsAuthenticated, UpdateView):
    model = InformasiPenerbangan
    template_name = 'admin-panel/component/form.html'
    form_class = InformasiPenerbanganForm
    success_url = reverse_lazy('informasi_penerbangan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'Edit InformasiPenerbangan'
        return context

class InformasiPenerbanganDeleteView(IsAuthenticated, DeleteView):
    model = InformasiPenerbangan
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('informasi_penerbangan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi Penerbangan'
        context['header_title'] = 'Delete Informasi Penerbangan'
        return context
