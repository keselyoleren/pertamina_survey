from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout

from config.permis import IsAuthenticated, IsLoginAuthenticated
from manage_user.form.login_form import LoginForm
from config.choice import RoleUser

class UserLoginView(IsLoginAuthenticated ,LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    def get_success_url(self) -> str:
        if self.request.user.role_user in [RoleUser.SUPER_ADMIN, RoleUser.DPPU]:
            return "/admin-panel/"
        return "/"

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LogoutCustomerView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutCustomerView, self).get(request, *args, **kwargs)
