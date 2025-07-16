from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from habit_tracker.models import Habit
from habit_tracker.serializers import HabitSerializer, PublishHabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    """Реализация представления привычек через ViewSet (полный crud)"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Присваиваем владельца привычки

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublishHabitAPIView(ListAPIView):
    """Реализация просмотра публичных привычек через ListAPIView."""
    serializer_class = PublishHabitSerializer
    queryset = Habit.objects.filter(sign_public=True)
