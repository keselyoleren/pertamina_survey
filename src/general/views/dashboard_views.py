# myapp/views.py


from config.permisson import IsAuthenticated

from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'admin-panel/index.html'