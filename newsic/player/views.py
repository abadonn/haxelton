from django.views.generic import View
from django.shortcuts import render_to_response
# Create your views here.

class Player(View):
    def get(self, request):
        return render_to_response('player.html', {})
