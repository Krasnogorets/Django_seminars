from django.contrib import admin
from .models import Author, Article, Comment


# Register your models here.

@admin.action(description="Сбросить количество просмотров в ноль")
def reset_views(modeladmin, request, queryset):
    queryset.update(views=0)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'views', 'published', 'date_of_creation']
    # fields = ['title', 'text', 'author', 'category', 'views', 'published', 'date_of_creation']
    readonly_fields = ['date_of_creation']
    ordering = ['-views']
    list_filter = ['published', 'category']
    search_fields = ['text']
    search_help_text = 'Поиск по полю текст статьи'
    actions = [reset_views]
    fieldsets = [(None,
                  {
                      'classes': ['wide'],
                      'fields': ['title'],
                  },),
                 (
                     'название статьи',
                     {
                         'classes': ['wide'],
                         'fields': ['category', 'author'],
                     },
                 ),
                 (
                     'текст статьи',
                     {
                         'classes': ['collapse'],
                         'description': 'текст статьи',
                         'fields': ['text'],
                     },
                 ),
                 (
                     'дополнительно',
                     {
                         'fields': ['views']
                     }
                 ),
                 (
                     'публикация',
                     {
                         'fields': ['published', 'date_of_creation'],
                     }
                 ),
                 ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'secondname', 'email', 'birthday']
    ordering = ['-name']
    readonly_fields = ['birthday']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'date_of_update', 'date_of_creation']
    ordering = ['-date_of_update']
    list_filter = ['date_of_update', 'author']
    search_fields = ['comment']
    search_help_text = 'Поиск по полю текста комментария'
    readonly_fields = ['date_of_creation','date_of_update']
    fieldsets = [(None,
                  {
                      'classes': ['wide'],
                      'fields': ['author'],
                  },),
                 (
                     'название статьи',
                     {
                         'classes': ['wide'],
                         'fields': ['article'],
                     },
                 ),
                 (
                     'текст комментария',
                     {
                         'classes': ['collapse'],
                         'description': 'текст комментария',
                         'fields': ['comment'],
                     },
                 ),

                 (
                     'даты',
                     {
                         'fields': ['date_of_update', 'date_of_creation'],
                     }
                 ),
                 ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
