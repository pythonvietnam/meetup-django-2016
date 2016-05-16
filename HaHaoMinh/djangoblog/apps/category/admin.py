from django.contrib import admin

# Register your models here.
from .models import CategoryModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_display_links = ["name", "slug"]
    list_filter = ["name", "slug"]
    search_fields = ["name", "slug"]

    class Meta:
        model = CategoryModel


admin.site.register(CategoryModel, CategoryAdmin)
