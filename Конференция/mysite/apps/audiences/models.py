from django.db import models


class Audience(models.Model):
    audience_number = models.IntegerField('Номер аудитории')
    capacity = models.IntegerField('Вместимость')

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


class Lecture(models.Model):
    audience = models.ForeignKey(Audience, on_delete=models.CASCADE)
    lecture_title = models.CharField('Название лекции', max_length=50)
    speaker_name = models.CharField('Имя спикера', max_length=50)
    start_time = models.DateTimeField('Время начала доклада')
    end_time = models.DateTimeField('Время конца доклада')

    def add_lecture(self, audience, lecture_title, speaker_name, start_time, end_time):
        self.audience = audience
        self.lecture_title = lecture_title
        self.speaker_name = speaker_name
        self.start_time = start_time
        self.end_time = end_time

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
