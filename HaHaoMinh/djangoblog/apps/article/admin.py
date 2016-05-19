from django.contrib import admin

# Register your models here.
from .models import ArticleModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "timestamp", "updated"]
    list_display_links = ["name", "updated"]
    list_filter = ["name", "category", "timestamp", "updated"]
    search_fields = ["name", "category", "timestamp", "updated", "content"]
    # Display field on admin create Article
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'height_field', 'width_field', 'content', 'category')
        }),
        # Can show advanced option field on here
        # ('Advanced options', {
        #     'classes': ('collapse',),
        #     'fields': ('registration_required', 'template_name'),
        # }),
    )

    class Meta:
        model = ArticleModel


admin.site.register(ArticleModel, ArticleAdmin)
