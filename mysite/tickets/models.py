from django.db import models
from django.urls import reverse


class Event(models.Model):
    idevent = models.AutoField(db_column='idEvent', primary_key=True, verbose_name='id')
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата мероприятия')
    title = models.CharField(max_length=150, verbose_name='Название мероприятия')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_events', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-idevent']
        db_table = 'event'


class Ticket(models.Model):
    idticket = models.AutoField(db_column='idTicket', primary_key=True, verbose_name='id')
    first_name = models.CharField(max_length=45, verbose_name='Имя')
    last_name = models.CharField(max_length=45, verbose_name='Фамилия')
    email = models.CharField(max_length=45, verbose_name='Адрес электронной почты')
    type = models.CharField(max_length=45, verbose_name='Тип')
    event_idevent = models.ForeignKey(Event, models.DO_NOTHING, db_column='Event_idEvent', verbose_name='Мероприятие')

    def __str__(self):
        return self.type + f' ({self.idticket})'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        db_table = 'ticket'
        unique_together = (('idticket', 'event_idevent'),)
