from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import Bn2EnSerializer
from pybengengphonetic import hinavro

discard_delim = ['<BGD', 'I <BGD', 'I<BGD', 'Place of Birth', 'Blood Group', 'Issue Date']


class Entry(object):
    def __init__(self, **kwargs):
        for field in ('text',):
            setattr(self, field, kwargs.get(field, None))


class Bn2EnView(viewsets.ViewSet):
    serializer_class = Bn2EnSerializer

    def list(self, request):
        req_text = str(request.data['text'])

        en_text = hinavro.parse(req_text).capitalize()
        entries = {
            1: Entry(text=en_text),
        }
        serializer = Bn2EnSerializer(instance=entries.values(), many=True)
        return Response(serializer.data)
