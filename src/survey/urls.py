# myapp/urls.py

from django.urls import path, include
from survey.views.question_views import *
from survey.views.responden_view import *
from survey.views.suervey_views import *


urlpatterns = [
    path("survey/", include([
        path('', SurveyListView.as_view(), name='survey-list'),
        path('create/', SurveyCreateView.as_view(), name='survey-create'),
        path('update/<int:pk>/', SurveyUpdateView.as_view(), name='survey-update'),
        path('delete/<int:pk>/', SurveyDeleteView.as_view(), name='survey-delete'),
    ])),

    path('responden/', include([
        path('', RespondenListView.as_view(), name='responden-list'),
        path('views/<int:pk>/', RespondenDetailView.as_view(), name='responden-detail'),
        path('delete/<int:pk>/', RespondenDeleteView.as_view(), name='responden-delete'),
        path('total/', TotalSurveyView.as_view(), name='responden-total'),
    ])),

    path("question/", include([
        path('<int:survey_id>', QuestionListView.as_view(), name='question-list'),
        path('<int:survey_id>/create/', QuestionCreateView.as_view(), name='question-create'),
        path('<int:survey_id>/update/<int:pk>/', QuestionUpdateView.as_view(), name='question-update'),
        path('<int:survey_id>/delete/<int:pk>/', QuestionDeleteView.as_view(), name='question-delete'),
    ]))
]