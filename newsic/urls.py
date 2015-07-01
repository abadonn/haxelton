"""newsic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from .player.views import player, GetMyPlaylist
from .accounts.views import Register, Login, LogMeIn, LogMeOut, Profile
from .news.views import TopicList


urlpatterns = [
    url(r'^api/topiclist', TopicList.as_view()),
    url(r'^api/login', LogMeIn.as_view()),
    url(r'^api/logout', LogMeOut.as_view()),
    url(r'^api/playlist', GetMyPlaylist.as_view()),
    url(r'^login$', Login.as_view()),
    url(r'^register$', Register.as_view()),
    url(r'^profile$', Profile.as_view()),
    url(r'', player),
]
