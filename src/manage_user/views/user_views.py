# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from config.permis import IsAuthenticated

from manage_user.form.user_form import AccountUserForm, UserForm
from manage_user.models import AccountUser
from config.smtp import Smtp


class AccountUserListView(IsAuthenticated, ListView):
    model = AccountUser
    template_name = 'admin-panel/users/list.html'
    context_object_name = 'list_users'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'List User'
        context['create_url'] = reverse_lazy('user-create')
        return context

class AccountUserCreateView(CreateView):
    model = AccountUser
    template_name = 'admin-panel/component/form.html'
    form_class = AccountUserForm
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'Tambah User'
        return context

    def form_valid(self, form):
        print(form.cleaned_data.get('email'))
        Smtp(reciept=form.cleaned_data.get('email')).create_authorized_recipient()
        return super().form_valid(form)

class AccountUserUpdateView(UpdateView):
    model = AccountUser
    template_name = 'admin-panel/component/form.html'
    form_class = UserForm
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'Edit User'
        return context

class AccountUserDeleteView(DeleteView):
    model = AccountUser
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'User'
        context['header_title'] = 'Delete User'
        return context
