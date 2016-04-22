from django.conf.urls import url
from .views import blog_detail, blog_list


urlpatterns = [
    url(r'^$', blog_list, name='blog'),
    url(r'^(?P<slug>[\w-]+)/$', blog_detail, name='detail'),
]

