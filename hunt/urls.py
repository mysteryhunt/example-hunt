from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    #
    url(r'^all/$', 'hunt.views.puzzles_view'),
    url(r'^(?P<puzzle>\w+)/$', 'hunt.views.puzzle_view'),
    url(r'^meta/(?P<metapuzzle>\w+)/$', 'hunt.views.metapuzzle_view'),
)
