from django.conf.urls import url, include
from . import views


urlpatterns = [# url(r'^$',views.diskusijos,name='diskusijos'),
                #url(r'^create/$',views.diskusijos_create),
                url(r'^(?P<id>\d+)/$',views.diskusijos_detail, name = 'detail'),
                url(r'^(?P<id>\d+)/edit/$',views.diskusijos_update, name='update'),
                url(r'^(?P<id>\d+)/delete/$',views.diskusijos_delete,),
                          

                ]
