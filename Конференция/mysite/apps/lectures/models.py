from django.db import models
from django.utils import timezone


class Audience(models.Model):
    audience_number = models.IntegerField('Номер аудитории', default=0)


class Lecture(models.Model):
    audience_number = models.ForeignKey(Audience, on_delete=models.CASCADE)
    lecture_title = models.CharField('Название лекции', max_length=50)
    speaker_name = models.CharField('Имя спикера', max_length=50)
    description = models.TextField('Описание', default='', max_length=150)
    start_time = models.DateTimeField('Время начала доклада', default=timezone.now())
    end_time = models.DateTimeField('Время конца доклада', default=timezone.now())

    def __str__(self):
        return self.lecture_title

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
