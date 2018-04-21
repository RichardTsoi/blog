from django.conf.urls import url

from .views import IndexView, ArticleDetailView, AboutView, ContactView, ArchiveView, CategoryView, TagView, SearchView
from .views import AddLikeView
from .feeds import ArticleRssFeed

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^article/(?P<id>[0-9]+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchiveView.as_view(), name='archive'),
    url(r'^category/(?P<category_id>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^all/rss/$', ArticleRssFeed(), name='rss'),
    url(r'^add_like/$', AddLikeView.as_view(), name='add_fav'),
]
