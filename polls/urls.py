from rest_framework_swagger.views import get_swagger_view

from . import views
from django.urls import path

schema_view = get_swagger_view(title='eVoting API description')

urlpatterns = [
    path('create/', views.CreatePollView.as_view(), name='create-poll'),
    path('', views.PollListView.as_view(), name='list-polls'),

    path('<str:id>/', views.PollUpdateRetrieveDestroyView.as_view(),
         name='detail-poll'),
]
