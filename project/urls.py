from django.conf.urls import patterns, url
from project.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),

    #url(r'^category/(?P<id>\w+)/$', category, name='category'),
    #url(r'^category_list/$', category_list, name='category_list'),
    url(r'^category_add/$', category_add, name='category_add'),

    #url(r'^item/(?P<id>\w+)/$', item, name='item'),
    url(r'^item_list/$', item_list, name='item_list'),
    url(r'^item_add/$', item_add, name='item_add'),

    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
)

