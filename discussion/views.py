import json
from django.http import HttpResponse
from rest_framework import viewsets
from discussion.models import HotPotato
from discussion.serializers import HotPotatoSerializer


class HotPotatoViewSet(viewsets.ModelViewSet):
    queryset = HotPotato.objects.all()
    serializer_class = HotPotatoSerializer


def hotpotato_list(request):
    qs = HotPotato.objects.all()
    data = [
        {
            "id": hotpotato.id,
            "author": hotpotato.author,
            "title": hotpotato.title,
            "content": hotpotato.content,
            "photo": hotpotato.photo,
        }
        for hotpotato in qs
    ]
    json_string = json.dumps(data)
    return HttpResponse(json_string)
