from django.shortcuts import render
import actions
import spoilr.models as spoilr_models
from django.conf import settings
import os
import logging

TEAMS_BASE = os.path.join(settings.HUNT_DATA_DIR, 'dev', 'docroot', 'teams')

# type argument IS A BAD HACK
# def puzzle_view(request, puzzle):
#     return render(request, 'hunt/puzzle.tmpl', {'title': 'Example', 'puzzle_template': 'puzzle/' + puzzle + '/index.tmpl', 'puzzle': puzzle, 'team': request.META['REMOTE_USER'], 'type': 'puzzle'})

# def metapuzzle_view(request, metapuzzle):
#     return render(request, 'hunt/puzzle.tmpl', {'title': 'Example', 'puzzle_template': 'puzzle/' + metapuzzle + '/index.tmpl', 'puzzle': metapuzzle, 'team': request.META['REMOTE_USER'], 'type': 'meta'})

# def puzzles_view(request):
#     team = spoilr_models.Team.objects.get(username=request.META['REMOTE_USER'])
#     puzzles = team.puzzles.all()
#     rounds = team.rounds.all()

#     return render(request, 'hunt/puzzles.tmpl', {'title': 'Puzzles for %s' % (team.name,),
#                                                  'puzzles': puzzles, 'rounds': rounds})

def puzzle_view(request, puzzle):
    puzzle_file = os.path.join(TEAMS_BASE, request.META['REMOTE_USER'], 'puzzle', puzzle, 'index.html')
    return render(request, 'hunt/static_file.tmpl', {'path': puzzle_file})

def round_view(request, round):
    round_file = os.path.join(TEAMS_BASE, request.META['REMOTE_USER'], 'puzzle', round, 'index.html')
    return render(request, 'hunt/static_file.tmpl', {'path':round_file})

def top_view(request):
    top_file = os.path.join(TEAMS_BASE, request.META['REMOTE_USER'], 'index.html')
    return render(request, 'hunt/static_file.tmpl', {'path': top_file})
