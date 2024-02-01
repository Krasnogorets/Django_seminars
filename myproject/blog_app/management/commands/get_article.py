from django.core.management.base import BaseCommand
from blog_app.models import Article
class Command(BaseCommand):
    help = "Get all articles."
    def handle(self, *args, **kwargs):
        articles = Article.objects.all()
        self.stdout.write(f'{articles}')