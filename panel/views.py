from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Source, Stream, RtmpSettings
from django.urls import reverse_lazy
from django.http import HttpResponse
import json
import requests




# Create your views here.


def write_config(request):
#Сбор параметров входящих и исходящих потоков
    cameras = []
    streams = []
    rtmps = []

    for obj in Source.objects.all():
    #Обходим все источники и записываем атрибуты в словарь
        para_source = {}
        para_source.update({
            'id':str(obj.id),
            'ip': str(obj.ip),
            'port':obj.port,
            'miface':str(obj.miface),
            'protocol':str(obj.protocol)
                     })
        cameras.append(para_source)


    for obj in Stream.objects.all():
    # Обходим все исходящие потоки и записываем атрибуты в словарь
        para_stream = {}
        para_stream.update({
            'id':str(obj.id),
            'video':{"cam":str(obj.video.id), "pid":int(obj.vpid)},
            'audio':{"cam":str(obj.audio.id), "pid":int(obj.apid)},
            'app':obj.app,
            'stream':obj.stream
        })

        streams.append(para_stream)


    for obj in RtmpSettings.objects.all():
        rtmps = {}
        protocols = []
        abrstreams = ((requests.get('http://192.168.1.247/panel/api/abrstreams/')).json())

        for item in list((obj.protocols.all()).values()):
            protocols.append(item.get('protocol'))


        rtmps.update(
            {
                "hash": "3",
                "interfaces": [],
                "login": "",
                "password": "",
                "duration": obj.duration,
                "chunk_count": obj.chunk_count,
                "dash_template": "TIME",
                "protocols": protocols,
                "apps": [],
                "abr": abrstreams
            }
        )



    # Дальше подставляем полученные словари для источников и исходящих потоков в конфиг нимбла
    #TODO вынести остальные важные параметры из конфига в задаваемые поля моделей
    config = {}
    config.update({
        "SyncResponse": {
                "status": "success",
                "StreamCheckerMode": False,
                "UniqueVisitors": False,
                "RoutesHash": "",
                "Routes": [],
                "IpRanges": [],
                "ServerAuthorizationProperties": {"ServerAuthPropertiesHash": "1"},
                "CamerasHash": "1",
                "Cameras": cameras,
                "StreamsHash": "2",
                "Streams": streams,
                "RtmpSettings": rtmps,
                "RtspSettings": {"hash": "0", "interfaces": []},
                "IcecastSettings": {"hash": "0", "interfaces": []},
                "LivePullSettings": {"hash": "0", "streams": []},
                "RtmpPublishSettings": {"hash": "0", "settings": []},
                "RtspPublishSettings": {"hash": "0", "settings": []},
                "ManagedTasks": {"hash": "0", "tasks": []},
                "HlsDRMSettings": {"hash": "0", "url": "", "key": "", "KeyServerSettings": {}},
                "HttpOriginApps": {"hash": "0", "apps": []},
                "Aliases": {"hash": "0", "settings": []},
                "DataSlicesInfo": {"hash": "1", "data_slices": [{"id": "42185", "tz": 0}]},
                "UDPSenderSettings": {"hash": "0", "settings": []},
                "PayPerPublishSettings": {"hash": "0", "url": "", "auth_group_interval": 500, "apps": []},
                "DvrSettings": {"hash": "0", "settings": []},
                "UserAgentGroupSettings": {"hash": "0", "settings": []},
                "RefererGroupSettings": {"hash": "0", "settings": []},
                "VideoEncodersInfo": {"hash": "0", "encoders": []},
                "AudioEncodersInfo": {"hash": "0", "encoders": []},
                "StreamOverrideSettings": {"hash": "0", "settings": []},
                "IcecastStreamSettings": {"hash": "0", "settings": []},
                "AuthHandlerSettings": {"hash": "1"},
                "ServerSettings": {"MaxCacheSize": 64, "MaxFileCacheSize": 4096, "LogMode": "info"}}
    })

    #Создаем описание конфигурации в формате JSON и пишем в файл
    config_data = json.dumps(config).replace(' ', '')
    config_file = open('/etc/nimble/rules.conf', 'w')
    config_file.write(config_data)
    config_file.close()
    # C помощью Nimble API перезаписываем конфигурацию
    #TODO как-то прямолинейно. Нужно задавать порт с помощью переменной и улучшить код
    requests.post('http://192.168.1.247:8088/manage/reload_config')

    #TODO это нужно обрабатывать JS и выводить сообщение
    return HttpResponse()


class IndexView(TemplateView):

    template_name = 'panel/index.html'

#Представления источников:
class SourcesList(ListView):
    model = Source


class SourceDetail(DetailView):
    model = Source


class SourceCreate(CreateView):
    model = Source
    fields = ['name', 'ip', 'port', 'miface', 'protocol']
    success_url = reverse_lazy('sources_list')

class SourceUpdate(UpdateView):
    model = Source
    fields = ['name', 'ip', 'port', 'miface', 'protocol']
    success_url = reverse_lazy('sources_list')

class SourceDelete(DeleteView):
    model = Source
    success_url = reverse_lazy('sources_list')

#Представления исходящих потоков

class StreamsList(ListView):
    model = Stream

class StreamDetail(DetailView):
    model = Stream

class StreamCreate(CreateView):
    model = Stream
    fields = '__all__'
    success_url = reverse_lazy('streams_list')

class StreamUpdate(UpdateView):
    model = Stream
    fields = '__all__'
    success_url = reverse_lazy('streams_list')

class StreamDelete(DeleteView):
    model = Stream
    success_url = reverse_lazy('streams_list')
