from django.conf.urls import url

from ..models import Tag
from ..views import(
        TagCreate, TagUpdate, TagDelete,
        TagList, TagPageList, TagDetail)

urlpatterns = [
    url(r'^$',
        TagList.as_view(),
        name='organizer_tag_list'),
    url(r'^create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),
    url(r'^(?P<page_number>\d+)/$',
        TagPageList.as_view(),
        name='organizer_tag_page'),
    url(r'^(?P<slug>[\w\-]+)/$',
        TagDetail.as_view(
            context_object_name='tag',
            model=Tag,
            template_name=(
                'organizer/tag_detail.html')),
        name='organizer_tag_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$',
        TagDelete.as_view(),
        name='organizer_tag_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update')
]