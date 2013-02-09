from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'page.views.home', name='home'),
    #url(r'', include("django_socketio.urls")),
    url(r'^chat/$', 'chat.views.home'),
    url(r'^node_api$', 'chat.views.node_api', name='node_api'),
    url(r'^accounts/singup/$', 'accounts.views.singup'),
    url(r'^accounts/profile/$', 'accounts.views.profile'),
    url(r'^accounts/login/$', 'accounts.views.login'),
    url(r'^social/', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/vlad/workspace/chat/bin/texnar/static'}),
)
