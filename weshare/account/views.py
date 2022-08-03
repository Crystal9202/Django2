from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import MyUserCreationForm


@login_required
def dashboard(request):
    return render(request , 'account/dashboard.html')

#會員註冊
def register(request):
    if request.method == "POST":
        user_form = MyUserCreationForm(request.POST)  #初始化form
        if user_form.is_valid():
            new_user = user_form.save(commit=False)#先創建一個空的，先別存
            new_user.set_password(
                user_form.cleaned_data['password1']  #類似hashpassword  #UserCreationForm 就能發現 password有 password1/password2
            )
            new_user.save()
            return render(request , 'account/register_done.html',{'new_user': new_user})
    else:  #get請求
        user_form = MyUserCreationForm()
    return render(request , 'account/register.html' , {'user_form':user_form})
