from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    url(r'^blog/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^blogauthor/$', views.BlogAuthorListView.as_view(), name='blogauthors'),
    url(r'^blogauthors/(?P<pk>\d+)$', views.BlogAuthorDetailView.as_view(), name='blog-author-detail'),
    url(r'^blog/newblog/$', views.new_blog, name='new-blog'),
    url(r'^blog/myblogs/$', views.my_blogs, name='my-blogs'),

]

urlpatterns += [
    url(r'^blog/(?P<pk>[-\w]+)/addcomment/$', views.add_comment, name='add-comment'),
]