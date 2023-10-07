# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.urls import reverse_lazy
from config.permis import IsAuthenticated, LoginRequiredMixin
from config.choice import RoleUser
from general.form.keluhan_form import KeluhanForm, TanggapanForm
from django.shortcuts import redirect

from general.models import Keluhan, Tanggapan



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
        context['btn_add'] = False
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
        context['btn_add'] = False
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
        context['btn_add'] = False
        context['header_title'] = 'Edit Keluhan'
        return context

class KeluhanDetailView(IsAuthenticated, DetailView):
    model = Keluhan
    template_name = 'admin-panel/keluhan/detail.html'
    context_object_name = 'keluhan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['btn_add'] = False
        context['form'] = TanggapanForm()
        context['header_title'] = 'Detail Keluhan Customer'
        context['tanggapan'] = self.object.tanggapan_set.all()
        return context


class KeluahnUpdateStatus(IsAuthenticated, View):
    def post(self, request, *args, **kwargs):
        keluhan = Keluhan.objects.get(pk=self.kwargs['pk'])
        keluhan.status = self.request.POST['status']
        keluhan.save()
        return redirect('keluhan-detail', pk=keluhan.pk)


class TanggapanView(IsAuthenticated, View):
    def post(self, request, *args, **kwargs):
        keluhan = Keluhan.objects.get(pk=self.kwargs['pk'])
        form = TanggapanForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.keluhan = keluhan
            form.save()
            return redirect('keluhan-detail', pk=keluhan.pk)
        return redirect('keluhan-detail', pk=keluhan.pk)

    def get(self, request, *args, **kwargs):
        tanggapan = Tanggapan.objects.get(pk=self.kwargs['pk'])
        tanggapan.delete()
        return redirect('keluhan-detail', pk=tanggapan.keluhan.pk)


class KeluhanDeleteView(DeleteView):
    model = Keluhan
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('keluhan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Keluhan'
        context['btn_add'] = False
        context['header_title'] = 'Delete Keluhan'
        return context
