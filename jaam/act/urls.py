from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.act.views',
                       url(r'^(?P<act_slug>[^\\]+)/$', 'details'),
)

