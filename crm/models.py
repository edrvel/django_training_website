from django.db import models


class Order(models.Model):
    order_id = models.DateTimeField(auto_now=True, verbose_name='Дата')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return f'Заказ {self.id}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
