from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', include('upload.urls')),
	(r'^i18n/', include('django.conf.urls.i18n')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'upload.views.home'),
    url(r'^about/', 'upload.views.about'),
    (r'^register/$', 'users.views.UserbetRegistration'),
    (r'^login/$', 'users.views.LoginRequest'),
    (r'^logout/$', 'users.views.LogoutRequest'),
    (r'^user/$', 'users.views.user'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),


		
)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#    )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)