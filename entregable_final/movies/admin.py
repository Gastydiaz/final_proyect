from django.contrib import admin

from movies.models import Movies,Studio,Director,Windows

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'duration', 'date')

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display= ('name', 'creation', 'place')
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display= ('name', 'films', 'birth', 'retired')

@admin.register(Windows)
class WindowsAdmin(admin.ModelAdmin):
    list_display= ('name','tittle','text')



