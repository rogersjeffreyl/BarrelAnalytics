from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'barrel.views.home'),
    url(r'^search/?', 'barrel.views.search'),
    url(r'^save_link/?', 'barrel.views.save_link'),
    url(r'^rm_link/?', 'barrel.views.rm_link'),
    url(r'^register/?', 'barrel.views.register'),
    url(r'^dashboard/?', 'barrel.views.dashboard'),
    url(r'^show_clicks/?', 'barrel.views.show_clicks'),
    url(r'^show_locations/?', 'barrel.views.show_locations'),
    url(r'^login/?', 'barrel.views.user_login'),
    url(r'^logout/?', 'barrel.views.user_logout'),
    url(r'^profile_trend/?', 'barrel.views.get_profile_trend'),

    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
