from django.conf.urls import url

from .views import(
        NewsLinkCreate, NewsLinkUpdate, StartupCreate,
        StartupUpdate, TagCreate, TagUpdate,
        startup_detail, startup_list, tag_detail,
        tag_list)

urlpatterns = [
    url(r'^newslink/create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
    url(r'^newslink/delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
    url(r'^newslink/update/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
    url(r'^startup/$',
        startup_list,
        name='organizer_startup_list'),
    url(r'^startup/create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),
    url(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    url(r'^startup/(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
    url(r'^tag/$',
        tag_list,
        name='organizer_tag_list'),
    url(r'^tag/create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
    url(r'^tag/(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update')
]