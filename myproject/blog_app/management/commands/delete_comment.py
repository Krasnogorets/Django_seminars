from django.core.management.base import BaseCommand
from blog_app.models import Comment


class Command(BaseCommand):
    help = "Delete comment by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='comment ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        comment = Comment.objects.filter(pk=pk).first()
        if comment is not None:
            comment.delete()
        self.stdout.write(f'комментарий с id={comment.pk} удален')