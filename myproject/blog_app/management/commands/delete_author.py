from django.core.management.base import BaseCommand
from blog_app.models import Author


class Command(BaseCommand):
    help = "Delete author by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            author.delete()
        self.stdout.write(f'автор {author} удален')
