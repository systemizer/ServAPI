from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('project.main.views',
    url(r'^$', 'index'),
    url(r'^survey/$', 'survey'),
)
