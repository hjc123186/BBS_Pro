from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import  models
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
import django_comments


@csrf_exempt
def index(request):
    bbs_list = models.BBS.objects.all()

    return render_to_response('index.html',{'bbs_list':bbs_list,'user':request.user})


def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id = bbs_id )
    return render_to_response('bbs_detail.html',{'bbs_obj':bbs})

@csrf_exempt
def sub_comment(request):
    # print "-->",request.POST
    bbs_id = request.POST.get('bbs_id')

    # bbs_id = request.POST.get('next')
    # bbs_id = request.POST.get('bbs_obj.id')
    print "bbs_id:",bbs_id

    comment = request.POST.get('comment_content')
    django_comments.models.Comment.objects.create(
        content_type_id = 7,
        object_pk = bbs_id,
        site_id = 1,
        user = request.user,
        comment = comment,

    )
    return HttpResponseRedirect('/detail/%s' % bbs_id)

@csrf_exempt
def login_view(request):
    # print '--->:',request.POST
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(username=username,password=password)
        # print  "user:",user
        if user and user.is_active:
            login(request,user)
            return HttpResponseRedirect('/index.html')
    return render_to_response('login.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/Login/')