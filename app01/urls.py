from  django.conf.urls import patterns,url,include

import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^index.html$',views.index),
    url(r'^detail/(\d+)/$',views.bbs_detail),
    url(r'sub_comment/$',views.sub_comment),
    url(r'bbs_pub/$',views.bbs_pub),
    url(r'bbs_sub/$',views.bbs_sub),

]