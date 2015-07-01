from datetime import datetime
from datetime import timedelta
import json
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
        yesterday = datetime.now() - timedelta(days=1)
        result = client.get('/me/tracks', created_at={
            'from': "{0}-{1}-{2} 00:00:00".format(yesterday.year,
                                                  yesterday.month,
                                                  yesterday.day) })
        user_id = request.user.id
        preferences = UserPreference.objects.all().filter(user__id=user_id)
        playlist = []
        for track in result:
            if self._is_valid_track(track, preferences) is not True:
                continue
            final_track = {
                "title": track.title,
                "description": track.description,
                "link": client.get(track.stream_url, allow_redirects=False).location
            }
            playlist.append(final_track)

        return HttpResponse(json.dumps(playlist), content_type="application/json")

    def _is_valid_track(self, track, preferences):

        for preference in preferences:
            publisher = "#{0}".format(preference.publisher)
            topic = "#{0}".format(preference.topic)

            if publisher in track.description and topic in track.description:
                return True
        return False
