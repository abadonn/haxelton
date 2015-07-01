import json
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


class Login(View):
    def get(self, request):
        return render_to_response('login.html', {})


class LogMeIn(View):
    def get(self, request):
        user = authenticate(username=request.GET.get("username"), password=request.GET.get("password"))
        response = user is not None and user.is_active
        if response:
            login(request, user)
            return HttpResponseRedirect(request.GET.get("next", "/"))
        return HttpResponse(json.dumps(response), content_type="application/json")

class LogMeOut(View):
    def get(self, request):
        logout(request)


class Register(View):
    def get(self, request):
        return render_to_response('register.html', {})


class Profile(View):
    def get(self, request):
        return render_to_response('profile.html', {})
