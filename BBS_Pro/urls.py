"""BBS_Pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import app01.urls
import django_comments.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(app01.urls)),
    url(r'^comments/',include(django_comments.urls)),
    url(r'accounts/Login/$','app01.views.login_view'),
    url(r'accounts/Logout/$','app01.views.logout_view'),
]
