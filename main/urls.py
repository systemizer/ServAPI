from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('project.main.views',
    url(r'^$', 'index'),
    url(r'^create/survey/','create_survey'),
    url(r'^create/question/','create_question'),
    url(r'^edit/survey/','edit_survey'),                       
    url(r'^publish/','publish_survey'),                       
)
