from django.db import models


class TableRow(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    jan = models.BooleanField(default=False, verbose_name='Январь')
    feb = models.BooleanField(default=False, verbose_name='Февраль')
    mar = models.BooleanField(default=False, verbose_name='Март')
    apr = models.BooleanField(default=False, verbose_name='Апрель')
    may = models.BooleanField(default=False, verbose_name='Май')
    jun = models.BooleanField(default=False, verbose_name='Июнь')
    jul = models.BooleanField(default=False, verbose_name='Июль')
    aug = models.BooleanField(default=False, verbose_name='Август')
    sep = models.BooleanField(default=False, verbose_name='Сентябрь')
    oct = models.BooleanField(default=False, verbose_name='Октябрь')
    nov = models.BooleanField(default=False, verbose_name='Ноябрь')
    dec = models.BooleanField(default=False, verbose_name='Декабрь')

    def __str__(self):
        return f'{self.title}'