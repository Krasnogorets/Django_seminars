"""
Создайте модель Автор. Модель должна содержать
следующие поля:
○ имя до 100 символов
○ фамилия до 100 символов
○ почта
○ биография
○ день рождения
Дополнительно создай пользовательское поле “полное
имя”, которое возвращает имя и фамилию.

Создайте модель Статья (публикация). Авторы из прошлой задачи могут
писать статьи. У статьи может быть только один автор. У статьи должны быть
следующие обязательные поля:
○ заголовок статьи с максимальной длиной 200 символов
○ содержание статьи
○ дата публикации статьи
○ автор статьи с удалением связанных объектов при удалении автора
○ категория статьи с максимальной длиной 100 символов
○ количество просмотров статьи со значением по умолчанию 0
○ флаг, указывающий, опубликована ли статья со значением по умолчанию
False

Создайте модель Комментарий.
Авторы могут добавлять комментарии к своим и чужим
статьям. Т.е. у комментария может быть один автор.
И комментарий относится к одной статье. У модели должны
быть следующие поля
○ автор
○ статья
○ комментарий
○ дата создания
○ дата изменения
"""
from django.db import models
from random import choice

from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()
    fullname = models.CharField(blank=True, null=True,max_length=203)

    def save(self, *args, **kwargs):
        self.fullname = self.secondname + " " + self.name
        return super().save(*args, **kwargs)

    # def full_name(self):
    #     return f'{self.secondname} {self.name}'
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_full',kwargs={'article_id': self.pk})
    def __str__(self):
        return self.title

    def get_summary(self):
        words = str(self.text).split()
        return f'{" ".join(words[:12])}...'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
