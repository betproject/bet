from django.conf.urls import patterns, url, include

 
urlpatterns = patterns('upload.views',
   url(r'^$', 'home'),
   
)