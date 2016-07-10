from django.contrib import admin

from .models import Career


class ArticleAdmin(admin.ModelAdmin):
  list_display = ["fullname", "timestamp", "email", "phone"]
  list_display_links = ["fullname"]
  list_filter = ["fullname", "gender", "email", "phone"]
  search_fields = ["fullname", "gender", "email", "phone"]

  class Meta:
    model = Career

admin.site.register(Career, ArticleAdmin)