from django.contrib import admin
from .models import Category, Post, Book


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'publish')
	prepopulated_fields = {'slug':('name', )}


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'publish')
	prepopulated_fields = {'slug':('title', )}


class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Book, BookAdmin)
