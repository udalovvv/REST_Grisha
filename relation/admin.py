from django.contrib import admin
from . import models


@admin.register(models.Mod)
class ModAdmin(admin.ModelAdmin):
    list_display = ["title_of_mod", "text_of_mod"]
    # filter_horizontal = ["comments"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text_of_comment", "mod"]


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["counter", "comment"]