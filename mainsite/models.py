from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    #文章的标题
    title = models.CharField(max_length=200)
    #文章的网址
    slug = models.CharField(max_length=200)
    #文章的内容
    body = models.TextField()
    #文章发表的时间，pub_date是以timezone.now的方式产生的，需要一个pytz模块
    #因此需要安装pip install pytz
    pub_date = models.DateTimeField(default=timezone.now)


    #文章要现实的顺序是以pub_date为依据
    class Meta:
        ordering = ('-pub_date',) 
    #提供这个类产生的资料项目，以文章标题当作现实的内容。
    #使用unicode 而不是str,让这个标题可以正确地现实中文标题
    def __str__(self):
        return self.title
