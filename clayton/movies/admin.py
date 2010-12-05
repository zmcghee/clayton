from django.contrib import admin
from clayton.movies.models import Venue, FilmLog

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state',)
    list_display_links = ('name',)
    list_filter = ('city', 'state',)
    search_fields = ['name']

class FilmLogAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'movie_title', 'release_year', 'rating',
        'is_nonfiction', 'is_repeat_viewing', 'venue',)
    list_display_links = ('movie_title',)
    list_filter = ('is_nonfiction', 'is_repeat_viewing', 'rating', 'venue', 'release_year',)
    search_fields = ['movie_title', 'imdb_id',]

admin.site.register(Venue, VenueAdmin)
admin.site.register(FilmLog, FilmLogAdmin)
