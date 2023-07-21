# myapp/views.py


from config.permis import IsAuthenticated

from django.views.generic import TemplateView


class DashboardView(IsAuthenticated, TemplateView):
    template_name = 'admin-panel/index.html'