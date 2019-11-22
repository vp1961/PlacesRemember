from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField('Название', max_length=50)
    location = models.PointField(srid=4326)
    comment = models.TextField('Комментарий')
    author = models.ForeignKey(User, default=1, verbose_name='пользователь', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Воспоминание"
        verbose_name_plural = "Воспоминания"

    def __str__(self):
        return self.name