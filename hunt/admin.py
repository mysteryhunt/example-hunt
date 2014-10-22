from django.contrib import admin
from .models import *

class Y2015TeamDataAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')
    search_fields = ['team__name']

admin.site.register(Y2015TeamData, Y2015TeamDataAdmin)

class Y2015PuzzleDataAdmin(admin.ModelAdmin):
    def puzzle_name(data):
        return data.puzzle.name
    puzzle_name.short_description = 'Puzzle Name'
    list_display = ('points_req', puzzle_name)
    search_fields = ['puzzle__name']
    ordering = ['points_req']

admin.site.register(Y2015PuzzleData, Y2015PuzzleDataAdmin)

class Y2015PuzzleLinkAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'puzzle1', 'puzzle2')
    search_fields = ['puzzle1', 'puzzle2']
    ordering = ['puzzle1__order', 'puzzle2__order']

admin.site.register(Y2015PuzzleLink, Y2015PuzzleLinkAdmin)

class Y2015PuzzleUnlockAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team', 'puzzle', 'reached', 'enough_points')
    list_filter = ('team__name', 'reached', 'enough_points')
    search_fields = ['team__name', 'puzzle__name', 'puzzle__round__name']
    ordering = ['team__name', 'puzzle__round__order', 'puzzle__order']
