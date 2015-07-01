from django.views.generic import View
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..accounts.models import UserPreference


import soundcloud

# Create your views here.

@login_required(login_url='/login')
def player(request):
    return render_to_response('player.html', {})


class GetMyPlaylist(View):
    def get(self, request):
        client = soundcloud.Client(
            client_id="584b42b093b0b2d2635491514da66665",
            client_secret='44c1678fb4320d6f765ec1e92068a3c2',
            username='newsicclient',
            password='thisisnewsic')
        """
        result = client.get('/me/tracks')
        track = client.get('/tracks/212801333')
        stream_url = client.get(track.stream_url, allow_redirects=False)
        print(stream_url.location)

        return HttpResponse(result.raw_data)
        """

        return "oh yeah"
