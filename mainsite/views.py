from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect #引入重定向
from datetime import datetime
from .models import Post



# Create your views here.
# def homepage(request):
#     posts = Post.objects.all()
#     post_lists = list()
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count)) + str(post) + "<hr>")
#         post_lists.append("<small>" + str(post.body)\
#             +"</small><br><br>")
#     return HttpResponse(post_lists)


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

#showpost函数用于，处理request请求，查看文章详情，考虑到有可能有自行输入错误网址
#以至于找不到文章的情形，除了在以Post.objects.get(slug=slug)收缩文章是加上例外
#时的处理，在发生例外的时候是用redirect的方法直接重定向到首页。

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')