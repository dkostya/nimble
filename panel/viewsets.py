from rest_framework import viewsets
from .models import Source, Stream, Iface, RtmpSettings, Protocols, ABRStream, ABRSource, Server
from .serializers import \
    SourceSerializer, StreamSerializer, IfaceSerialyzer, \
    RtmpSettingsSerializer, ProtocolsSerializer, ABRStreamSerializer, ABRSourceSerializer, ServerSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class IfaceViewSet(viewsets.ModelViewSet):
    queryset = Iface.objects.all()
    serializer_class = IfaceSerialyzer

class RtmpSettingsViewSet(viewsets.ModelViewSet):
    queryset = RtmpSettings.objects.all()
    serializer_class = RtmpSettingsSerializer

class ProtocolsViewSet(viewsets.ModelViewSet):
    queryset = Protocols.objects.all()
    serializer_class = ProtocolsSerializer

class ABRstreamViewSet(viewsets.ModelViewSet):
    queryset = ABRStream.objects.all()
    serializer_class = ABRStreamSerializer

class ABRSourceViewSet(viewsets.ModelViewSet):
    queryset = ABRSource.objects.all()
    serializer_class = ABRSourceSerializer

class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
