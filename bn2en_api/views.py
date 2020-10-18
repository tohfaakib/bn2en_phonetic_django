from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import Bn2EnSerializer
from pybengengphonetic import hinavro


class Entry(object):
    def __init__(self, **kwargs):
        for field in ('text',):
            setattr(self, field, kwargs.get(field, None))


class Bn2EnView(viewsets.ViewSet):
    serializer_class = Bn2EnSerializer

    def list(self, request):
        en_text = hinavro.parse(request.data['text']).capitalize()
        entries = {
            1: Entry(text=en_text),
        }
        serializer = Bn2EnSerializer(instance=entries.values(), many=True)
        return Response(serializer.data)
