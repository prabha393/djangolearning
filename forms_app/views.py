from django.shortcuts import render
from django.views.generic import View
from .forms import UserInfoForm

class UserInfo(View):

    def get(self, request):
        
        form = UserInfoForm()
        return render(request, "user-info.html", {'form' : form})
