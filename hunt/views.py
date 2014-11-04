from django.shortcuts import render
import actions
import spoilr.models as spoilr_models

# type argument IS A BAD HACK
def puzzle_view(request, puzzle):
    return render(request, 'hunt/puzzle.tmpl', {'title': 'Example', 'puzzle_template': 'puzzle/' + puzzle + '/index.tmpl', 'puzzle': puzzle, 'team': request.META['REMOTE_USER'], 'type': 'puzzle'})

def metapuzzle_view(request, metapuzzle):
    return render(request, 'hunt/puzzle.tmpl', {'title': 'Example', 'puzzle_template': 'puzzle/' + metapuzzle + '/index.tmpl', 'puzzle': metapuzzle, 'team': request.META['REMOTE_USER'], 'type': 'meta'})

def puzzles_view(request):
    team = spoilr_models.Team.objects.get(username=request.META['REMOTE_USER'])
    puzzles = team.puzzles.all()
    rounds = team.rounds.all()

    return render(request, 'hunt/puzzles.tmpl', {'title': 'Puzzles for %s' % (team.name,),
                                                 'puzzles': puzzles, 'rounds': rounds})
