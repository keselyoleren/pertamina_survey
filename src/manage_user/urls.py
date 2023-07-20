# myapp/urls.py

from django.urls import path, include
from manage_user.views.customer_views import *
from manage_user.views.login_views import LogoutView, UserLoginView
from manage_user.views.ptm_location_view import *
from manage_user.views.instansi_views import *
from manage_user.views.user_views import *

urlpatterns = [
    path("auth/", include([
        path("login/", UserLoginView.as_view(), name="admin-login"),
        path("logout/", LogoutView.as_view(), name="admin-logout"),
    ])),
    path("customer/", include([
        path('', CustomerListView.as_view(), name='customer-list'),
        path('create/', CustomerCreateView.as_view(), name='customer-create'),
        path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
        path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),
    ])),
    path("ptm-location/", include([
        path('', PTMListView.as_view(), name='ptm-list'),
        path('create/', PTMCreateView.as_view(), name='ptm-create'),
        path('update/<int:pk>/', PTMUpdateView.as_view(), name='ptm-update'),
        path('delete/<int:pk>/', PTMDeleteView.as_view(), name='ptm-delete'),
    ])),

    path("instansi/", include([
        path('', InstansiListView.as_view(), name='instansi-list'),
        path('create/', InstansiCreateView.as_view(), name='instansi-create'),
        path('update/<int:pk>/', InstansiUpdateView.as_view(), name='instansi-update'),
        path('delete/<int:pk>/', InstansiDeleteView.as_view(), name='instansi-delete'),
    ])),

    path("user/", include([
        path('', AccountUserListView.as_view(), name='user-list'),
        path('create/', AccountUserCreateView.as_view(), name='user-create'),
        path('update/<int:pk>/', AccountUserUpdateView.as_view(), name='user-update'),
        path('delete/<int:pk>/', AccountUserDeleteView.as_view(), name='user-delete'),
    ])),
]
