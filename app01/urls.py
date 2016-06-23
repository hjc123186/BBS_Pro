from  django.conf.urls import patterns,url,include

import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^detail/(\d+)/$',views.bbs_detail)
]