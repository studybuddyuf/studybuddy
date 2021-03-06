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
 
    # Create User
    url(r'^register/$', 'createPage.views.register_user'),

    # Update Profile Page
    url(r'^editprofile/$', 'profilePage.views.update_profile'),
	url(r'^profile/$', 'profilePage.views.profile'),

    # Search
    url(r'^search/$', 'searchPage.views.search'),
    url(r'^doSearch/$', 'searchPage.views.doSearch'),

    #email
    url(r'^emailtest/', 'searchPage.views.emailtest'),
    url(r'^emailResults/', 'searchPage.views.emailResults'),

    # Home page
    url(r'^home/$', 'homePage.views.main'),
    url(r'^acceptRequest/$', 'homePage.views.acceptRequest'),
    url(r'^rejectRequest/$', 'homePage.views.rejectRequest'),
    url(r'viewProfile/$', 'homePage.views.viewProfile'),
	
	# Schedule
	url(r'^schedule/$', 'schedulePage.views.main'),
	url(r'^editschedule/$', 'schedulePage.views.edit'),
	url(r'^editschedule/removeClass/$', 'schedulePage.views.removeClass'),
    url(r'^editschedule/addClass/$', 'schedulePage.views.addClass'),
    url(r'^editschedule/removePersonal/$', 'schedulePage.views.removePersonal'),
    url(r'^editschedule/addPersonal/$', 'schedulePage.views.addPersonal'),

    # Search Result
    url(r'^searchResult/$', 'searchPage.views.doSearch'),
	url(r'^searchResultTest/$', 'searchPage.views.searchResultTest'),

    # User authenticaton
    url(r'^auth/$', 'startPage.views.auth_view'),
    url(r'^logout/$', 'startPage.views.logout'),
)
