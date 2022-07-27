from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate , login

from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(   #認證
                request , 
                username=cd['username'],   #取得用戶資料
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request , user)
                    return HttpResponse(
                        'Authentucated successfully')
                else:
                    return HttpResponse('Disable account') #帳號密碼錯誤
            else:
                return HttpResponse('Invalid login')  #用戶不存在
    
    else:
        form = LoginForm()
        return render(request , 'account/login.html' , {'form':form})
