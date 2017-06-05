from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
#from rest_framework.urlpatterns import format_suffix_patterns
#from snippets.views import SnippetViewSet, UserViewSet, api_root
#from rest_framework import renderers

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
'''
snippet_list = SnippetViewSet.as_view({
    'get':'list',
    'post': 'create' 
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
    'patch': 'partial_update'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'    
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]'''
