import json
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import UserPreference


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
        return HttpResponseRedirect( "/login?error=invalid")


class LogMeOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

class Register(View):
    def get(self, request):
        return render_to_response('register.html', {})


class Profile(View):
    def get(self, request):
        return render_to_response('profile.html', {})

    def post(self, request):
        print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        for topic, publishers in data["data"].items():
            for publisher in publishers:
                preference = UserPreference(topic=topic, publisher=publishers, user=request.user)
                preference.save()

        return HttpResponse("ok", content_type="application/json")
