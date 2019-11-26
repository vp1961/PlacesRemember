from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Place(models.Model):
    name = models.CharField('Название', max_length=50)
    location = models.PointField(srid=4326)
    comment = models.TextField('Комментарий')
    author = models.ForeignKey(User, default=1, verbose_name='пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place_detail', args=[str(self.id)])
