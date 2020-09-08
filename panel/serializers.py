from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Source, Stream, Iface, RtmpSettings, Protocols, ABRStream, ABRSource, Server


class IfaceSerialyzer(serializers.ModelSerializer):

    class Meta:
        model = Iface
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = '__all__'


class StreamSerializer(serializers.ModelSerializer):

    video = serializers.SlugRelatedField(queryset=Source.objects.all(), slug_field='name')
    audio = serializers.SlugRelatedField(queryset=Source.objects.all(), slug_field='name')

    class Meta:
        model = Stream
        fields = '__all__'

class ProtocolsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Protocols
        fields = '__all__'

class RtmpSettingsSerializer(serializers.ModelSerializer):


    protocols = serializers.SlugRelatedField(many=True, queryset=Protocols.objects.all(), slug_field='protocol')

    class Meta:
        model = RtmpSettings
        fields = '__all__'

class ABRSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ABRSource
        fields = ('app', 'stream')

class ABRStreamSerializer(WritableNestedModelSerializer):

    streams = ABRSourceSerializer(many=True)

    class Meta:
        model = ABRStream
        fields = ('id', 'app', 'stream', 'order', 'streams')

class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'
