from django.shortcuts import render


def puzzle_view(request, puzzle):
    return render(request, 'hunt/puzzle.tmpl', {'title': 'Example', 'puzzle_template': 'puzzle/' + puzzle + '/index.tmpl'})
