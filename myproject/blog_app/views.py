from django.shortcuts import render, get_object_or_404
from .models import Author, Article, Comment
from .forms import AuthorForm, AuthorForm1, ArticleForm, CommentForm


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            comment = form.cleaned_data['comment']
            author = form.cleaned_data['author']
            author_id = Author.objects.filter(name=author).values('id')
            Comment.objects.create(article_id=article_id, comment=comment,author_id=author_id)
            message = 'комментарий сохранён'
            return render(request, 'blog_app/post_full.html', {'article': article, 'comments': comments,
                                                               'authors': authors, 'form': form, 'message': message})
    else:
        form = CommentForm()
        message = 'Заполните комментарий'
        return render(request, 'blog_app/post_full.html', {'article': article, 'comments': comments,
                                                           'authors': authors, 'form': form, 'message': message})
    return render(request, 'blog_app/post_full.html', {'article': article, 'comments': comments,
                                                       'authors': authors, 'form': form, 'message': message})


def author_input(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            secondname = form.cleaned_data['secondname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            fullname = f'{secondname} {name}'
            Author.objects.create(name=name, secondname=secondname, email=email, bio=bio, birthday=birthday,
                                  fullname=fullname)
            message = 'Пользователь сохранён'
            return render(request, 'blog_app/author_input.html', {'message': message})
    else:
        form = AuthorForm()
        message = 'Заполните форму'
        return render(request, 'blog_app/author_input.html', {'form': form, 'message': message})


def author_input_1(request):
    if request.method == 'POST':
        form = AuthorForm1(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form.save()
            message = 'Пользователь сохранён'
            return render(request, 'blog_app/author_input.html', {'form': form, 'message': message})
    else:
        form = AuthorForm1()
        message = 'Заполните форму'
        return render(request, 'blog_app/author_input.html', {'form': form, 'message': message})


def article_input(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form.save()
            message = 'статья сохранёна'
            return render(request, 'blog_app/article_input.html', {'form': form, 'message': message})
    else:
        form = ArticleForm()
        message = 'Заполните форму'
        return render(request, 'blog_app/article_input.html', {'form': form, 'message': message})
