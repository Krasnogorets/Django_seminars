from django.core.management.base import BaseCommand
from blog_app.models import Article


class Command(BaseCommand):
    help = "Get all articles."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        article = Article.objects.filter(pk=pk).first()
        self.stdout.write(f'{article}')
