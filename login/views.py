#-*- coding:utf8 -*-
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
def login_view(request):
    #
    errors = ''
    if request.method=="GET":
        form = LoginForm()
        return render_to_response('login/login.html',{'form':form})
    else:
        # print '--->:',request.POST
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                login(request,user)
                # return HttpResponseRedirect('/index.html')
                next = request.GET.get('next')
                # print "+++>" , next
                return HttpResponseRedirect('%s' % next)
            else:
                errors = "用户或密码错误"
            #     return render_to_response('login/login.html',{'form':form})
    return render_to_response('login/login.html',{'form':form,'errors':errors})

@login_required()
@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/Login/')



