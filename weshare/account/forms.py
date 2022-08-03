from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):   #自己創建一個 MyUserCreationForm  #繼承 UserCreationForm

    class Meta:
        model = User
        fields = ("username" , "first_name" , "email")   #show出要顯示的東西