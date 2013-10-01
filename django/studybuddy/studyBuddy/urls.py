from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyBuddy.views.home', name='home'),
    # url(r'^studyBuddy/', include('studyBuddy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Start pgae
    url(r'^$', 'startPage.views.main'),
    
    # Create Page
    url(r'^$', 'profilePage.views.main'), 

    # Home pgae
    url(r'^home/$', 'homePage.views.main'),

    # User authenticaton
    url(r'^auth/$', 'startPage.views.auth_view'),
    url(r'^logout/$', 'startPage.views.logout'),
    url(r'^register/$', 'profilePage.views.register_user'),
)
