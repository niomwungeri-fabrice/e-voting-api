from rest_framework_swagger.views import get_swagger_view

from . import views
from django.urls import path

schema_view = get_swagger_view(title='eVoting API description')

urlpatterns = [
    path('docs/', schema_view),
    path('create/', views.CreatePollViewSet, name='create-poll'),
]
