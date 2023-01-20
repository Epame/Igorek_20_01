from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание полное")
    technology = models.CharField('технология', max_length=50)
    image = models.FileField(upload_to='img/')

    def __str__(self):
        #строковое отображение в админке списка названия
        return self.title[:50]




