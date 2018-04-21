from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

from operation.forms import CommentForm
from .models import *
from .forms import ContactForm
from operation.models import UserComment, ReplyComment, UserLike
from .catelog import catelog

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class IndexView(View):
    def get(self, request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = Article.objects.all().order_by('-add_time')

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(objects, 5, request=request)

        article_list = p.page(page)

        return render(request, 'index.html', {'article_list': article_list})


class ArticleDetailView(View):
    def get(self, request, id):
        form = CommentForm()
        article = Article.objects.get(pk=id)
        article.click_numbers += 1
        article.save()
        title_tree = catelog(article.content)
        has_like = False
        if request.user.is_authenticated:
            if UserLike.objects.filter(user=request.user, fav_id=article.id):
                has_like = True
        comment_list = UserComment.objects.filter(article=article)
        return render(request, 'single.html', {'article': article,
                                               'comment_list': comment_list,
                                               'form': form,
                                               'title_tree': title_tree,
                                               'has_like': has_like})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    # 留言板功能
    def post(self, request):
        form = ContactForm(request.POST)
        to_email = '632540458@qq.com'
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            text = request.POST.get('message', '')
            send_status = send_mail(subject, '名字：{0} \n联系邮箱：{1} \n留言:{2}'.format(name, email, text),
                                    settings.DEFAULT_FROM_EMAIL, [to_email])
            if send_status:
                return redirect('/')
        return render(request, 'contact.html', {'form': form})


class ArchiveView(View):
    def get(self, request, year, month):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = Article.objects.filter(add_time__year=year, add_time__month=month).order_by('-add_time')

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(objects, 5, request=request)

        article_list = p.page(page)
        return render(request, 'index.html', {'article_list': article_list})


class CategoryView(View):
    def get(self, request, category_id):
        cate = Category.objects.get(pk=category_id)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = Article.objects.filter(category=cate).order_by('-add_time')

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(objects, 5, request=request)

        article_list = p.page(page)
        return render(request, 'index.html', {'article_list': article_list})


class TagView(View):
    def get(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = Article.objects.filter(tag=tag).order_by('-add_time')

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(objects, 5, request=request)

        article_list = p.page(page)
        return render(request, 'index.html', {'article_list': article_list})


# 搜索功能视图函数
class SearchView(View):
    def get(self, request):
        key_word = request.GET.get('keyword', '')
        if key_word:
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            objects = Article.objects.filter(Q(title__icontains=key_word) | Q(content__icontains=key_word)).order_by('-add_time')

            # Provide Paginator with the request object for complete querystring generation

            p = Paginator(objects, 5, request=request)

            article_list = p.page(page)
            return render(request, 'index.html', {'article_list': article_list})
        return render(request, 'index.html', {'error_msg': '请输入关键词'})


# 文章点赞功能
class AddLikeView(View):
    def post(self, request):
        article_id = request.POST.get('article_id', '0')
        article = Article.objects.get(pk=article_id)
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type="application/json")

        if int(article_id) > 0:
            user_like = UserLike(user=request.user, fav_id=article_id)
            user_like.save()
            article.like_numbers += 1
            article.save()
            return HttpResponse('{"status": "success", "msg": "点赞成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status": "success", "msg": "点赞出错"}', content_type="application/json")

