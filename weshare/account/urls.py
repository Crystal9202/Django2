from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #post views
    path('login/' , auth_views.LoginView.as_view(template_name="account/login.html"),  name="login"),   #as_view()  是一個函數   #默認是使用registration底下的html，但也可以透過在as_view(templates_name="account/login.html") 指定執行那裡的html
]