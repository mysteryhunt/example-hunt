from django.db import models
from spoilr.models import *

class Y2015TeamData(models.Model):
    team = models.OneToOneField(Team)
    points = models.IntegerField(default=0, verbose_name='Points')

    def __str__(self):
        return '%s (%d)' % (self.team.name, self.points)

    class Meta:
        verbose_name = '2015 team data'
        verbose_name_plural = '2015 team data'

class Y2015PuzzleData(models.Model):
    puzzle = models.OneToOneField(Puzzle)
    points_req = models.IntegerField(default=0, verbose_name='Points required')

    def __str__(self):
        return '%s (req %d)' % (self.puzzle.name, self.points_req)

    class Meta:
        verbose_name = '2015 puzzle data'
        verbose_name_plural = '2015 puzzle data'

class Y2015PuzzleLink(models.Model):
    puzzle1 = models.ForeignKey(Puzzle, related_name='+')
    puzzle2 = models.ForeignKey(Puzzle, related_name='+')

    def __str__(self):
        return '%s <-> %s' % (self.puzzle1.name, self.puzzle2.name)

    class Meta:
        unique_together = ('puzzle1', 'puzzle2')
        ordering = ['puzzle1__order', 'puzzle2__order']
        verbose_name = '2015 puzzle link'
        verbose_name_plural = '2015 puzzle links'

class Y2015PuzzleUnlock(models.Model):
    team = models.ForeignKey(Team)
    puzzle = models.ForeignKey(Puzzle)
    reached = models.BooleanField(default=False)
    enough_points = models.BooleanField(default=False)

    def __str__(self):
        return '%s on %s: reached=%s enough_points=%s' % (
                team, puzzle, reached, enough_points)

    class Meta:
        verbose_name = '2015 puzzle unlock status'
        verbose_name_plural = '2015 puzzle unlock statuses'
