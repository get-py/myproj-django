from django.contrib import admin

from discussion.models import HotPotato, Comment, Tag


@admin.register(HotPotato)
class HotPotatoAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
