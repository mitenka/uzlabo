from django.contrib import admin

from ideas.models import (
    Category,
    Image,
    Idea,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'status', 'author', 'upvotes', 'downvotes', 'created_at')
