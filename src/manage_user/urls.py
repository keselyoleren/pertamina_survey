# myapp/urls.py

from django.urls import path, include
from manage_user.views.customer_views import CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView


urlpatterns = [
    path("customer/", include([
        path('', CustomerListView.as_view(), name='customer-list'),
        path('create/', CustomerCreateView.as_view(), name='customer-create'),
        path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
        path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),
    ])),
]
