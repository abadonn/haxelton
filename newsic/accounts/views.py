from django.views.generic import View
from django.shortcuts import render_to_response
# Create your views here.


class Login(View):
    def get(self, request):
        return render_to_response('login.html', {})


class Register(View):
    def get(self, request):
        return render_to_response('register.html', {})
