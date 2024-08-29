from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField('Название фильма', max_length=30)
    description = models.TextField('Описание фильма')
    review = models.CharField('Отзыв', max_length=100)

    def __str__(self):
        return self.title
