# myapp/urls.py

from django.urls import path, include
from general.views.informasi_views import InformasiCreateView, InformasiListView, InformasiListView, InformasiUpdateView, InformasiDeleteView
from general.views.keluhan_views import KeluhanCreateView, KeluhanListView, KeluhanUpdateView, KeluhanDeleteView
urlpatterns = [
    path("informasi/", include([
        path('', InformasiListView.as_view(), name='informasi-list'),
        path('create/', InformasiCreateView.as_view(), name='informasi-create'),
        path('update/<int:pk>/', InformasiUpdateView.as_view(), name='informasi-update'),
        path('delete/<int:pk>/', InformasiDeleteView.as_view(), name='informasi-delete'),
    ])),
    path("keluhan/", include([
        path('', KeluhanListView.as_view(), name='keluhan-list'),
        path('create/', KeluhanCreateView.as_view(), name='keluhan-create'),
        path('update/<int:pk>/', KeluhanUpdateView.as_view(), name='keluhan-update'),
        path('delete/<int:pk>/', KeluhanDeleteView.as_view(), name='keluhan-delete'),
    ])),
]
