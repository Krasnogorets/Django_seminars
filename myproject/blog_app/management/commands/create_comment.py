from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from blog_app.models import Comment, Author, Article
from random import choice,shuffle
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        comments = Comment(author=choice(Author.objects.all()),
                           article=choice(Article.objects.all()),
                           comment=" ".join(sorted(lorem_ipsum.words(10).split(), key=lambda k: random.random())))
        comments.save()
        self.stdout.write(f'{comments} создан')
