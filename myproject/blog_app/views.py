from django.shortcuts import render, get_object_or_404
from .models import Author, Article,Comment


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author, published=True).order_by('-id')[:5]
    num = len(articles)
    return render(request, 'blog_app/index.html', {'author': author, 'articles': articles, 'num': num})


def post_full(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('-date_of_update')
    authors = Author.objects.all()
    article.views += 1
    article.save()
    return render(request, 'blog_app/post_full.html', {'article': article,'comments':comments,
                                                       'authors': authors})
