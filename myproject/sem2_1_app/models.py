"""
Создайте модель для запоминания бросков монеты: орёл или
решка.
Также запоминайте время броска
"""

from django.db import models
from random import choice





class CoinModel(models.Model):
    SIDE = ('heads','tails')
    side = models.CharField(max_length=5,default=choice(SIDE))
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.side} {self.time}'

    @staticmethod
    def getstatistics(n):
        query = CoinModel.objects.all()[-n:]
        heads_count = sum(i.side == "heads" for i in query)
        tails_count = n - heads_count
        return {'heads': heads_count, 'tails': tails_count}
