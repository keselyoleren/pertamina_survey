# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.choice import RoleUser
from config.permis import IsAuthenticated, LoginRequiredMixin
from config.smtp import Smtp
from django.contrib import messages
from general.form.informasi_form import InformasiForm

from general.models import Informasi
from manage_user.models import AccountUser

class InformasiListView(IsAuthenticated, ListView):
    model = Informasi
    template_name = 'admin-panel/informasi/list.html'
    context_object_name = 'informasi_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role_user == RoleUser.SUPER_ADMIN:
            return super().get_queryset().order_by('-created_at')
        return super().get_queryset().filter(user__ptm_location=self.request.user.ptm_location).order_by('-created_at')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Informasi'
        context['header_title'] = 'List Informasi'
        context['create_url'] = reverse_lazy('informasi-create')
        context['btn_add'] = True
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

    def form_valid(self, form):
        template = 'email/informasi.html'
        context = {
            'customer':form.cleaned_data.get('customer'),
            'perihal':form.cleaned_data.get('perihal'),
            'informasi':form.cleaned_data.get('informasi'),
        }
        
        for user in AccountUser.objects.filter(role_user=RoleUser.CUSTOMER, customer=form.cleaned_data.get('customer')):
            Smtp(
                template=template,
                subject='Informasi',
                reciept=[user.email],
                context=context
            ).send_mail()        
        messages.success(self.request, "informasi berhasi dikirim")
        return super().form_valid(form)

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
