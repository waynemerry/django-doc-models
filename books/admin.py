from django.contrib import admin

# Register your models here.


from .models import Publisher, Blog, Author, Entry, Book


class Publisher_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'website']


class Blog_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tagline']


class Author_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


class Entry_Admin(admin.ModelAdmin):
    list_display = ['id', 'headline', 'pub_date']


class Book_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publication_date']


admin.site.register(Publisher, Publisher_Admin)
admin.site.register(Blog, Blog_Admin)
admin.site.register(Author, Author_Admin)
admin.site.register(Entry, Entry_Admin)
admin.site.register(Book, Book_Admin)
