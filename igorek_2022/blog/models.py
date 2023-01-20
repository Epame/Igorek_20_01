from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('Назв. категории', max_length=30)


class Post(models.Model):
    title = models.CharField('Название', max_length=150)
    body = models.TextField('Описание')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modifield = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title[:50]


class Comment(models.Model):
    author = models.CharField('Автор', max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author[:50]
