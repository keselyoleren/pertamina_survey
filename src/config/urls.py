"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from general.views.customer_suervey_views import SaveSurveyView
from general.views.customer_views import CreateInformasiPenerbangan, DashboardCustomerView, DeleteInformasiPenerbangan, DetailInformasiCreateView, DetailSuerveCustomerView, InformasiCustomerView, InformasiPenerbanganCustomerView, KeluhanCustomerDeleteView, KeluhanCustomerListView, KeluhanCustomerUpdateView, KeluhanCustomerView, ReplayKeluhanVIew, SurveyCustomerListView, UpdateInformasiPenerbangan

from general.views.dashboard_views import DashboardView
from manage_user.views.login_views import ChangePasswordAdminView, CustomPasswordChangeView, LogoutCustomerView, LogoutView, ProfileUserApiView, UserLoginView

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path("admin-panel/", include([
        path("survey/", include('survey.urls')),
        path("dashboard", DashboardView.as_view(), name="dashboard-admin"),
        path('general/', include('general.urls')),
        path('manage-user/', include('manage_user.urls')),
    ])),
    path('', DashboardCustomerView.as_view(), name="dashboard-customer"),
    path("keluhan/", include([
        path('create/', KeluhanCustomerView.as_view(), name="keluhan-customer"),
        path('<int:pk>/views', KeluhanCustomerUpdateView.as_view(), name="keluhan-customer-view"),
        path('<int:pk>/update', ReplayKeluhanVIew.as_view(), name="keluhan-customer-update"),
        path('<int:pk>/delete', KeluhanCustomerDeleteView.as_view(), name="keluhan-customer-delete"),
        path("", KeluhanCustomerListView.as_view(), name="keluhan-customer-list"),
    ])),
    path('informasi', InformasiCustomerView.as_view(), name="informasi-customer"),
    path("informasi-penerbangan/", include([
        path('', InformasiPenerbanganCustomerView.as_view(), name="informasi-penerbangan-customer"),
        path('create/', CreateInformasiPenerbangan.as_view(), name="informasi-penerbangan-customer-create"),
        path('<int:pk>/update/', UpdateInformasiPenerbangan.as_view(), name="informasi-penerbangan-customer-update"),
        path('<int:pk>/delete/', DeleteInformasiPenerbangan.as_view(), name="informasi-penerbangan-customer-delete"),
    ])),

    path('informasi/<int:pk>/', DetailInformasiCreateView.as_view(), name="informasi-detail-customer"),
    path('survey', SurveyCustomerListView.as_view(), name="survey-customer"),
    path('survey/<int:pk>/', DetailSuerveCustomerView.as_view(), name="survey-detail-customer"),
    path('save_survey/', SaveSurveyView.as_view(), name="save-survey"),
    path("auth/", include([
        path("login/", UserLoginView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(), name="logout"),
        path("change-password/", CustomPasswordChangeView.as_view(), name="change-password"),
        path('change-password-admin/<int:user_id>/', ChangePasswordAdminView.as_view(), name="change-password-admin"),
        path('logout-customer', LogoutCustomerView.as_view(), name="logout-customer"),
        path('profile/', ProfileUserApiView.as_view(), name='profile'),
    ])),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)