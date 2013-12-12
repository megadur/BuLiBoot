# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import HomePageView
from BuLiApp.views import BestenlisteView, SpieltagView, NewsView, UserFormView, FormView, FormHorizontalView, FormInlineView, PaginationView,  ImpressumView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'demo.views.home', name='home'),
#     # url(r'^demo/', include('demo.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^BuLiBoot$', HomePageView.as_view(), name='home'),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^bestenliste$', BestenlisteView.as_view(), name='bl'),
    url(r'^spieltag$', SpieltagView.as_view(), name='st'),
    url(r'^news$', NewsView.as_view(), name='news'),
    url(r'^user$', UserFormView.as_view(), name='form'),
    url(r'^impressum', ImpressumView.as_view(), name='form'),
 
    url(r'^form$', FormView.as_view(), name='form'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
)
