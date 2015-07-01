import json
from django.http import HttpResponse
from django.views.generic import View

from .models import Topic

class TopicList(View):
    def get(self, request):
        topics = {}
        for topic in Topic.objects.all():
            publishers = []
            for publisher in topic.publishers.all():
                publishers.append(publisher.name)
            topics[topic.name] = publishers

        return HttpResponse(json.dumps(topics), content_type="application/json")
