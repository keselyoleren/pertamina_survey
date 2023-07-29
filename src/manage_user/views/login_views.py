from webbrowser import get
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib import messages

from config.permis import IsAuthenticated, IsLoginAuthenticated, LoginRequiredMixin
from manage_user.form.login_form import LoginForm, ProfileForm
from django.views.generic.edit import UpdateView
from config.choice import RoleUser
from manage_user.models import AccountUser

class UserLoginView(IsLoginAuthenticated ,LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    def get_success_url(self) -> str:
        if self.request.user.role_user in [RoleUser.SUPER_ADMIN, RoleUser.DPPU]:
            return "/admin-panel/dashboard"
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


class ProfileUserApiView(LoginRequiredMixin, UpdateView):
    model = AccountUser
    template_name = 'admin-panel/component/form.html'
    form_class = ProfileForm
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['header'] = 'Profile'
        context['header_title'] = 'Update Profile'
        return context

    def get_object(self, queryset=None):
        return self.request.user

    def get_template_names(self):
        if self.request.user.role_user ==  RoleUser.CUSTOMNER:
            self.template_name = 'auth/profile.html'
        return super().get_template_names()

    def get_success_url(self):
        # Redirect to the profile page after successful form submission
        messages.success(self.request, "Profile berhasil di update")
        if self.request.user.role_user ==  RoleUser.CUSTOMNER:
            return '/'
        return '/admin-panel/dashboard'
