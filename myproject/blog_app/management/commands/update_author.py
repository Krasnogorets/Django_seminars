from django.core.management.base import BaseCommand
from blog_app.models import Author


class Command(BaseCommand):
    help = "Update author name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        author = Author.objects.filter(pk=pk).first()
        author.name = name
        author.save()
        self.stdout.write(f'автор с id={author.pk} обновлен')
