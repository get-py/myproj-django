from django.contrib import admin

from news.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article
        fields = "__all__"