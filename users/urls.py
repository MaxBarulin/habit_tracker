from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user'),
    ]