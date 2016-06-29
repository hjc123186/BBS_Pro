from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
def login_view(request):
    # print '--->:',request.POST
    # if request.method=="POST":
    #     form = LoginForm(request.POST)
    #     user = authenticate(username='username',password='password')
    #     if form.is_valid() and user.is_active:
    #         login(request,user)
    #         return HttpResponseRedirect('/index.html')
    # else:
    #     form = LoginForm()
    form = LoginForm()
    return render_to_response('login.html',{'form':form})


