from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import  models
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout


@csrf_exempt
def index(request):
    bbs_list = models.BBS.objects.all()

    return render_to_response('index.html',{'bbs_list':bbs_list})


def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id = bbs_id )
    return render_to_response('bbs_detail.html',{'bbs_obj':bbs})

@csrf_exempt
def sub_comment(request):
    print "-->",request.POST
    next = request.POST.get('next')
    return HttpResponseRedirect('/%s' % next)

@csrf_exempt
def login(request):
    print '--->:',request.POST
    if request.method=="POST":
        username = request.POST.get('name','')
        password = request.POST.get('password','')
        user = authenticate(username=username,password=password)
        print  "user:",user
        if user and user.is_active:
            login(request,user)
            print "BBBBB"
            return HttpResponseRedirect('/')
    print "ccccc"
    return render_to_response('login.html')

    # user = authenticate(username=request.POST['username'],password=request.POST['password'])
    # if user is not None:
    #     login(request,user)
    #     print request.user
    #     return list_prodect(request)
    # else:
    #     return store_view(request)

@csrf_exempt
def logout(request):
    logout(request)
    return HttpResponseRedirect('login.html')