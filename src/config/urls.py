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
from general.views.customer_views import DashboardCustomerView, InformasiCustomerView, KeluhanCustomerView, SuerveCustomerView

from general.views.dashboard_views import DashboardView
from manage_user.views.login_views import LogoutCustomerView, LogoutView, UserLoginView

urlpatterns = [
    path('', DashboardCustomerView.as_view(), name="dashboard-customer"),
    path('keluhan', KeluhanCustomerView.as_view(), name="keluhan-customer"),
    path('informasi', InformasiCustomerView.as_view(), name="informasi-customer"),
    path('survey', SuerveCustomerView.as_view(), name="survey-customer"),
    path("auth/", include([
        path("login/", UserLoginView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(), name="logout"),
        path('logout-customer', LogoutCustomerView.as_view(), name="logout-customer"),
    ])),
    path('superadmin/', admin.site.urls),
    path("admin-panel/", include([
        path('general/', include('general.urls')),
        path('manage-user/', include('manage_user.urls')),
        path("", include('survey.urls')),
        path("", DashboardView.as_view(), name="dashboard-admin"),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)