from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^puzzle/(?P<puzzle>\w+)/$', 'hunt.views.puzzle_view'),
    url(r'^round/(?P<round>\w+)/$', 'hunt.views.round_view'),
    url(r'^$', 'hunt.views.top_view')
#    url(r'^all/$', 'hunt.views.puzzles_view'),
#    url(r'^meta/(?P<metapuzzle>\w+)/$', 'hunt.views.metapuzzle_view'),
)
