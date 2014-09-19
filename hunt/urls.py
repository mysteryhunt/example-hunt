from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    #
    url(r'^(?P<puzzle>\w+)/$', 'hunt.views.puzzle_view'),
)
