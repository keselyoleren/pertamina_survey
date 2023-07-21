from django.views.generic import TemplateView

class DashboardCustomerView(TemplateView):
    template_name = 'customer/index.html'