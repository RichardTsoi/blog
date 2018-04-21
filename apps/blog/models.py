from datetime import datetime

from django.shortcuts import reverse
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags

from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='文章分类')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='文章标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=150, verbose_name='文章标题')
    content = RichTextUploadingField()
    excerpt = models.CharField(max_length=50, null=True, blank=True, verbose_name='文章摘要')
    like_numbers = models.IntegerField(default=0, verbose_name='点赞数')
    click_numbers = models.IntegerField(default=0, verbose_name='点击量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.content)[:50]
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.pk})
