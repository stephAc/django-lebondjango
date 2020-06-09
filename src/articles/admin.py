from django.contrib import admin

from .models import Articles, Category, Town

admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Town)
