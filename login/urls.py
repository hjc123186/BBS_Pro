from  django.conf.urls import patterns,url,include
from login.views import login_view,logout_view

urlpatterns = [
    url(r'accounts/Login/$',login_view),
    url(r'accounts/Logout/$',logout_view),
]