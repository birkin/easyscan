# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()

urlpatterns = patterns('',

    # url( r'^', include('easyscan_app.urls_app') ),

    url( r'^request/$',  'easyscan_app.views.request_def', name=u'request_url' ),

    url( r'^info/$',  'easyscan_app.views.info', name=u'info_url' ),

    url( r'^shib_login/$',  'easyscan_app.views.shib_login', name=u'shib_login_url' ),
    url( r'^logout/$',  'easyscan_app.views.shib_logout', name=u'logout_url' ),

    url( r'^confirmation/$',  'easyscan_app.views.confirmation', name=u'confirmation_url' ),

    url( r'^stats_api/v1/$',  'easyscan_app.views.stats_v1', name=u'stats_v1_url' ),

    url( r'^admin/try_again/$',  'easyscan_app.views.try_again', name=u'try_again_url' ),
    url( r'^admin/try_again/confirm/(?P<scan_request_id>[^/]+)/$',  'easyscan_app.views.try_again_confirmation', name=u'try_again_confirmation_url' ),

    url( r'^dev_josiah_easyscan.js/$',  'easyscan_app.views.easyscan_js', name=u'easyscan_js_url' ),  # replaces hardcoded urls for easy local development
    url( r'^dev_josiah_request_item.js/$',  'easyscan_app.views.request_item_js', name=u'request_item_js_url' ),  # replaces hardcoded urls for easy local development

    url( r'^version/$',  'easyscan_app.views.version', name=u'version_url' ),

    url(r'^admin/', include(admin.site.urls)),

    url( r'^$',  RedirectView.as_view(pattern_name=u'info_url') ),

)
