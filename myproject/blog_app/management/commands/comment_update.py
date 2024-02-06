from django.core.management.base import BaseCommand
from blog_app.models import Comment


class Command(BaseCommand):
    help = "Update comment by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='comment ID')
        parser.add_argument('text', type=str, help='comment text')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        comment_txt = kwargs.get('text')
        comment = Comment.objects.filter(pk=pk).first()
        comment.comment = comment_txt
        comment.save()
        self.stdout.write(f'comment с id={comment.pk} обновлен')
