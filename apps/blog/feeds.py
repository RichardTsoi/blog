__author__ = 'Tsoingkam'
__date__ = '2018/4/18 17:53'

from django.contrib.syndication.views import Feed
from .models import Article


class ArticleRssFeed(Feed):
    title = 'RichardTsoi的个人博客项目'
    link = '/'
    description = 'RichardTsoi个人博客文章演示项目'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return '%s[%s]' % (item.title, item.category)

    def item_description(self, item):
        return item.content
