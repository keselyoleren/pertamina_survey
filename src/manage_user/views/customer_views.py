# myapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from config.permis import IsAuthenticated
from manage_user.form.customer_form import CustomerForm
from manage_user.models import Customer

class CustomerListView(IsAuthenticated, ListView):
    model = Customer
    template_name = 'admin-panel/customer/list.html'
    context_object_name = 'customer_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Customer'
        context['header_title'] = 'List Customer'
        context['create_url'] = reverse_lazy('customer-create')
        return context

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'admin-panel/component/form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Customer'
        context['header_title'] = 'Tambah Customer'
        return context

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'admin-panel/component/form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Customer'
        context['header_title'] = 'Edit Customer'
        return context

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'admin-panel/component/delete.html'
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Customer'
        context['header_title'] = 'Delete Customer'
        return context
