from django.contrib import admin
from clayton.books.models import Author, BookLog

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'given_name',]

class BookLogAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_finished'
    list_display = ('date_finished', 'book_title', 'author', 'is_nonfiction', 'is_repeat_reading',)
    list_display_links = ('book_title',)
    list_filter = ('is_nonfiction', 'is_repeat_reading',)
    search_fields = ['book_title', 'isbn_10', 'isbn_13',]

admin.site.register(Author, AuthorAdmin)
admin.site.register(BookLog, BookLogAdmin)