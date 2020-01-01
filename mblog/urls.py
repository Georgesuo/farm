"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainsite.views import homepage, showpost

urlpatterns = [
    #后面不跟任何字符串的，都去url呼叫homepage函数
    url(r'^$',homepage),
    #将所有post/开头的网址后面的字符串都找出来，当做是第二个参数传递给showpost这个函数。
    url(r'^post/(\w+)$', showpost),
    url(r'^admin/', admin.site.urls),
]
