from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('project.main.views',
    url(r'^$', 'index'),
    url(r'^create/survey/','create_survey'),
    url(r'^create/question/','create_question'),
    url(r'^take/survey/','take_survey'),                   
    url(r'^edit/survey/','edit_survey'),                       
    url(r'^publish/','publish_survey'),                       
    url(r'^dashboard/','dashboard'),                       
    url(r'^view/survey/','view_survey'),                       
    url(r'^view/meta/','view_meta'), #for api reasons                       
    url(r'^view/all-surveys/','view_all_surveys'), #for api reasons                       
)
