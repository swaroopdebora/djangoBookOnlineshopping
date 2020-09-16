from django.contrib import admin
from .models import Book, Category

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
