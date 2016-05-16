from django.contrib import admin

# Register your models here.
from .models import ArticleModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "timestamp", "updated"]
    list_display_links = ["name", "updated"]
    list_filter = ["name", "category", "timestamp", "updated"]
    search_fields = ["name", "category", "timestamp", "updated", "content"]

    class Meta:
        model = ArticleModel


admin.site.register(ArticleModel, ArticleAdmin)
