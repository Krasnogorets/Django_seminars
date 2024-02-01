from random import choice

from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from blog_app.models import Article, Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        authors = Author.objects.all()
        for i in range(0, 5):
            article = Article(title=lorem_ipsum.words(10),
                              text=lorem_ipsum.paragraph(),
                              author=choice(authors),
                              category=f'обычная',
                              )
            article.save()
            self.stdout.write(f'{article.title} создана')
