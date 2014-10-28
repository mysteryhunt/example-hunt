import spoilr.actions as spoilr_actions
import models
import spoilr.models as spoilr_models
import logging
import spoilr.log as log

def grant_points(team, amount, reason, ctx=''):
    msg = "gained %d points from solving (%s)" % (amount, reason)
    logging.info("grant %d points to %s (%s)", amount, team.url, reason)
    log.team_log(team, "gained-points", msg, ctx)
    td = models.Y2015TeamData.objects.get(team=team)
    pre = td.points
    td.points = td.points + amount
    td.save()
    for puzzle_data in models.Y2015PuzzleData.objects.filter(points_req__lte=td.points):
        # faster/riskier to additionally filter by points_req__gt=pre?
        puzzle = puzzle_data.puzzle
        unlocks = models.Y2015PuzzleUnlock.objects.filter(team=team, puzzle=puzzle)
        if unlocks:
            unlock = unlocks.get()
            unlock.enough_points = True
            unlock.save()
            if unlock.reached:
                spoilr_actions.release_puzzle(team, puzzle, reason)
                spoilr_actions.release_round(team, puzzle.round, "team can access puzzle %s in round and has enough points (%d)" % (puzzle.name, td.points)
        else:
            models.Y2015PuzzleUnlock(team=team, puzzle=puzzle, enough_points=True).save()

def puzzle_reached(team, puzzle, reason):
    unlocks = models.Y2015PuzzleUnlock.objects.filter(team=team, puzzle=puzzle)
    if unlocks:
        unlock = unlocks.get()
        unlock.reached = True
        unlock.save()
        if unlock.enough_points:
            spoilr_actions.release_puzzle(team, puzzle, reason)
    else:
        models.Y2015PuzzleUnlock(team=team, puzzle=puzzle, reached=True).save()

def reach_linked_puzzles(team, puzzle):
    for edge in models.Y2015PuzzleLink.objects.filter(puzzle1=puzzle):
        puzzle_reached(team, edge.puzzle2, 'connected to "%s"' % puzzle.name)
    for edge in models.Y2015PuzzleLink.objects.filter(puzzle2=puzzle):
        puzzle_reached(team, edge.puzzle1, 'connected to "%s"' % puzzle.name)

def update_deep(team, metapuzzle):
    points = models.Y2015MetapuzzleData.objects.get(metapuzzle=metapuzzle).points
    grant_points(team, points, "Team solved meta %s" % (metapuzzle,), metapuzzle.url)

spoilr_actions.subscribe(spoilr_actions.metapuzzle_answer_correct_message,
                         update_deep)

spoilr_actions.subscribe(spoilr_actions.puzzle_answer_correct_message,
                         reach_linked_puzzles)
logging.info("subscribed!")
