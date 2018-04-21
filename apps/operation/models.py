from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from blog.models import Article
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


# 用户点赞模型
class UserLike(models.Model):
    user = models.ForeignKey(User)
    fav_id = models.IntegerField(default=0, verbose_name='文章数据ID')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户点赞'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s(%s)' % (self.user.username, self.fav_id)


class UserComment(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    comment = RichTextUploadingField(config_name='custom')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s(%s)' % (self.user.username, self.comment[:10])


# 回复评论模型
class ReplyComment(models.Model):
    article = models.ForeignKey(Article)
    parent_comment = models.ForeignKey(UserComment)
    to_user = models.ForeignKey(User, related_name='to_user', default='')
    user = models.ForeignKey(User, related_name='from_user', default='')
    text = RichTextUploadingField(config_name='custom')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='回复时间')

    class Meta:
        verbose_name = '回复评论'
        verbose_name_plural = verbose_name


