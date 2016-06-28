from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updatad_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy is too lazy.')
    photo = models.ImageField("uplooad_img/",default='upload_img/user-1.jpg')

    def __unicode__(self):
        return self.user.username