from django.conf.urls import patterns, url
 
urlpatterns = patterns('upload.views',
   url(r'^$', 'home'),
)