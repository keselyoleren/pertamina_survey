# myapp/urls.py

from django.urls import path, include
from general.views.informasi_penerbangan_views import * 
from general.views.informasi_views import * 
from general.views.keluhan_views import * 
urlpatterns = [
    path("informasi/", include([
        path('', InformasiListView.as_view(), name='informasi-list'),
        path('create/', InformasiCreateView.as_view(), name='informasi-create'),
        path('update/<int:pk>/', InformasiUpdateView.as_view(), name='informasi-update'),
        path('delete/<int:pk>/', InformasiDeleteView.as_view(), name='informasi-delete'),
    ])),
    path("informasi-penerbangan/", include([
        path('', InformasiPenerbanganListView.as_view(), name='informasi_penerbangan-list'),
        path('create/', InformasiPenerbanganCreateView.as_view(), name='informasi_penerbangan-create'),
        path('update/<int:pk>/', InformasiPenerbanganUpdateView.as_view(), name='informasi_penerbangan-update'),
        path('delete/<int:pk>/', InformasiPenerbanganDeleteView.as_view(), name='informasi_penerbangan-delete')
    ])),
    path("keluhan/", include([
        path('', KeluhanListView.as_view(), name='keluhan-list'),
        path('create/', KeluhanCreateView.as_view(), name='keluhan-create'),
        path('update/<int:pk>/', KeluhanUpdateView.as_view(), name='keluhan-update'),
        path('delete/<int:pk>/', KeluhanDeleteView.as_view(), name='keluhan-delete'),
    ])),
]
