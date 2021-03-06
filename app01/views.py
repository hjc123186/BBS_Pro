#-*- coding:utf8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import  models
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import django_comments
from forms import   BBS_sub_form
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

@login_required()
@csrf_exempt
def index(request):
    bbs_list = models.BBS.objects.all().order_by("-id")
    bbs_categories = models.Category.objects.all()
    paginator = Paginator(bbs_list,10)
    page = request.GET.get('page')
    try:
        bbs = paginator.page(page)
    except PageNotAnInteger:
        bbs = paginator.page(1)
    except EmptyPage:
        bbs = paginator.page(paginator.num_pages)

    return render_to_response('index.html',{
        'bbs_list':bbs,
        'user':request.user,
        'bbs_categories':bbs_categories,
    })

@login_required()
def category(request,cate_id):
    bbs_list = models.BBS.objects.filter(category__id=cate_id).order_by('-id')
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',{
        'bbs_list':bbs_list,
        'user':request.user,
        'bbs_categories':bbs_categories,
        'cate_id':int(cate_id),
    },
    context_instance=RequestContext(request)
                              )

@login_required()
def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id = bbs_id )
    bbs_categories = models.Category.objects.all()
    # cate_id = models.Category.objects.filter(category = BBS_category )
    return render_to_response('bbs_detail.html',{
        'bbs_obj':bbs,
        'user':request.user,
        'bbs_categories':bbs_categories,
    })

@login_required()
@csrf_exempt
def sub_comment(request):
    # print "-->",request.POST
    bbs_id = request.POST.get('bbs_id')

    # bbs_id = request.POST.get('next')
    # bbs_id = request.POST.get('bbs_obj.id')
    print "bbs_id:",bbs_id

    comment = request.POST.get('comment_content').strip()
    print "comment:",comment
    if comment is not  None and len(comment) > 0 :
        django_comments.models.Comment.objects.create(
            content_type_id = 7,
            object_pk = bbs_id,
            site_id = 1,
            user = request.user,
            comment = comment,
        )
    return HttpResponseRedirect('/detail/%s' % bbs_id)

@login_required()
def bbs_pub(request):
    form = BBS_sub_form()
    return render_to_response('bbs_pub.html' , {'user':request.user,'form':form})

@login_required()
@csrf_exempt
def bbs_sub(request):
    if request.method == "POST":
        form = BBS_sub_form(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            author = models.BBS_user.objects.get(user__username=request.user)
            title = request.POST.get('title')
            category = request.POST.get('category')
            summary = request.POST.get('summary')
            # print ',===>',request.POST.get('category')
            bbs = models.BBS.objects.create(
                category = models.Category.objects.get(id=category),
                title = title,
                summary = summary,
                content = content,
                author = author,
                view_count = 1,
                ranking = 1,
            )
            # return render_to_response('bbs_pub.html' , {'user':request.user,'form':form})
            return HttpResponseRedirect('/detail/%s' % bbs.id)
    else:
            form = BBS_sub_form()
    return render_to_response('bbs_pub.html' , {'user':request.user,'form':form})
# @csrf_exempt
# def login_view(request):
#     # print '--->:',request.POST
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username,password=password)
#         if user and user.is_active:
#             login(request,user)
#             return HttpResponseRedirect('/index.html')
#     return render_to_response('login.html')

# @login_required()
# @csrf_exempt
# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/accounts/Login/')