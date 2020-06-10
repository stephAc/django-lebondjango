from django.contrib import admin

from .models import Articles, Category, Town


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "town", "accepted", "timestamp")
    readonly_fields = ["timestamp"]
    ordering = ["timestamp", "accepted"]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Category)
admin.site.register(Town)
