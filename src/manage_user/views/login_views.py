from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout

from config.permisson import AdminLoginViewMixin
from manage_user.form.login_form import LoginForm

class UserLoginView(AdminLoginViewMixin ,LoginView):
    template_name = 'admin-panel/auth/login.html'
    form_class = LoginForm

    def get_success_url(self) -> str:
        return "/admin-panel/"

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/admin-panel/manage-user/auth/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)