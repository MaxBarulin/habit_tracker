from django.urls import path
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import HabitViewSet, PublishHabitAPIView

app_name = HabitTrackerConfig.name

router = DefaultRouter()
router.register(prefix=r"habit", viewset=HabitViewSet, basename='habit')

urlpatterns = [
    path('publish_habit_list/', PublishHabitAPIView.as_view(permission_classes=[IsAuthenticated]),
         name='publish_habit_list'),
] + router.urls
