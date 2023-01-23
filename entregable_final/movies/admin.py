from django.contrib import admin

from movies.models import Movies,Studio,Director

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'duration')
#admin.site.register(Movies)
admin.site.register(Studio)
admin.site.register(Director)

