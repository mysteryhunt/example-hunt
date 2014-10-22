import spoilr.actions

def grant_points(team, amount, reason):
    logger.info("grant %d points to %s (%s)", amount, team.url, reason)
    td = Y2015TeamData.objects.get(team=team)
    pre = td.points
    td.points = td.points + amount
    td.save()
    for puzzle_data in Y2015PuzzleData.objects.filter(points_req__lte=td.points):
        # faster/riskier to additionally filter by points_req__gt=pre?
        puzzle = puzzle_data.puzzle
        unlocks = Y2015PuzzleUnlock.objects.filter(team=team, puzzle=puzzle)
        if unlocks:
            unlock = unlocks.get()
            unlock.enough_points = True
            unlock.save()
            if unlock.reached:
                actions.release_puzzle(team, puzzle, reason)
        else:
            Y2015PuzzleUnlock(team=team, puzzle=puzzl, enough_points=True).save()

def puzzle_reached(team, puzzle, reason):
    unlocks = Y2015PuzzleUnlock.objects.filter(team=team, puzzle=puzzle)
    if unlocks:
        unlock = unlocks.get()
        unlock.reached = True
        unlock.save()
        if unlock.enough_points:
            actions.release_puzzle(team, puzzle, reason)
    else:
        Y2015PuzzleUnlock(team=team, puzzle=puzzl, reached=True).save()

def reach_linked_puzzles(team, puzzle):
    for edge in Y2015PuzzleLink.objects.filter(puzzle1=puzzle):
        puzzle_reached(team, edge.puzzle2, 'connected to "%s"' % puzzle.name)
    for edge in Y2015PuzzleLink.objects.filter(puzzle2=puzzle):
        puzzle_reached(team, edge.puzzle1, 'connected to "%s"' % puzzle.name)

actions.subscribe(
        actions.puzzle_answer_correct_message,
        reach_linked_puzzles)
