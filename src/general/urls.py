# myapp/urls.py

from django.urls import path, include
from general.views.informasi_views import InformasiCreateView, InformasiListView, InformasiListView, InformasiUpdateView, InformasiDeleteView

urlpatterns = [
    path("informasi/", include([
        path('', InformasiListView.as_view(), name='informasi-list'),
        path('create/', InformasiCreateView.as_view(), name='informasi-create'),
        path('update/<int:pk>/', InformasiUpdateView.as_view(), name='informasi-update'),
        path('delete/<int:pk>/', InformasiDeleteView.as_view(), name='informasi-delete'),
    ])),
]
