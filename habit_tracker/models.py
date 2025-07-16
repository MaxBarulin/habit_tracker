from django.db import models


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Пользователь")
    location = models.CharField(max_length=255, verbose_name='Место привычки', help_text='Введите место для привычки')
    time = models.TimeField(verbose_name='Время выполнения привычки', help_text='Введите время в формате (12:30)')
    action = models.CharField(max_length=510, verbose_name='Действие привычки', help_text='Введите действие привычки')
    sign_pleasant_habit = models.BooleanField(verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('habit_tracker.Habit', on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='Связанная привычка')
    periodicity = models.PositiveIntegerField(verbose_name='Периодичность привычки. в днях',
                                              help_text='Выберите период привычки в днях.', default=1,
                                              choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение', help_text='Вознаграждение', null=True,
                              blank=True)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение (не больше 120сек)',
                                                   help_text='Введите время выполнения привычки (не больше 120сек)')
    sign_public = models.BooleanField(verbose_name='Признак публичной привычки')

    def __str__(self):
        return f"{self.action}, id {self.id}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
