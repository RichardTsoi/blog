from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import CommentForm, ReplyCommentForm
from blog.models import Article
from .models import UserComment, ReplyComment


class CommentView(View):
    def post(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        user = request.user
        form = CommentForm(request.POST)
        if form.is_valid():
            text = request.POST.get('comment', '')
            user_comment = UserComment()
            user_comment.comment = text
            user_comment.user = user
            user_comment.article = article
            user_comment.save()
            return redirect('/article/{0}'.format(article.id))
        return render(request, 'single.html', {'msg': '评论填写出错'})


class ReplyCommentView(View):
    def get(self, request, article_id, comment_id):
        form = ReplyCommentForm()
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_id)
            user_comment = UserComment.objects.get(pk=comment_id)
            return render(request, 'reply_comment.html', {'article': article,
                                                          'user_comment': user_comment,
                                                          'form': form})
        return render(request, 'users/login.html')

    def post(self, request, article_id, comment_id):
        article = Article.objects.get(pk=article_id)
        user_comment = UserComment.objects.get(pk=comment_id)
        from_user = request.user
        to_user = user_comment.user
        form = ReplyCommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('text', '')
            reply_comment = ReplyComment()
            reply_comment.article = article
            reply_comment.parent_comment = user_comment
            reply_comment.to_user = to_user
            reply_comment.user = from_user
            reply_comment.text = content
            reply_comment.save()
            return redirect('/article/{0}'.format(article.id))
        return render(request, 'reply_comment.html', {'msg': '回复评论出错'})


