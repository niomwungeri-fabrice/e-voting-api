"""evoting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from accounts import views
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='eVoting API description')

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/polls/', include('polls.urls')),
    path('api/v1/users/create/', views.CreateAccountView.as_view(),
         name='user-register'),
    path('api/v1/users/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/users/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/users/', views.UserListView.as_view(),
         name='user-list'),
    path('api/v1/users/<uuid:id>/', views.UserDetailView.as_view(),
         name='user-detail'),
    path('api/v1/users/me/', views.CurrentUserView.as_view(),
         name='me'),
    path('api/v1/docs/', schema_view),

]
