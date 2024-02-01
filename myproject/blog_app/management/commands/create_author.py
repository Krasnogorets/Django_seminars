from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from blog_app.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(0,5):
            author = Author(name=f'автор_{i}',
                            secondname=f'фамилия_{i}',
                            email=f'author_{i}@mail.ru',
                            bio=lorem_ipsum.words(30),
                            birthday = '2000-11-01')
            author.save()
            self.stdout.write(f'{author.name} создан')



