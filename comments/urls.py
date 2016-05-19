from django.conf.urls import url, include
from . import views


urlpatterns = [
                url(r'^(?P<id>\d+)/delete_comment/$',views.comment_delete,),
                          

                ]
