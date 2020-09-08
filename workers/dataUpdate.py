import requests
from panel.models import Source, Stream, Server

# Request example:

# curl -vvv http://127.0.0.1:8082/manage/mpeg2ts_status
# Response example:
# {"Cameras":[{"id":"1","st":"offline","tr":"0","bw":"0","pmts":[]},{"id":"2","st":"offline","tr":"0","bw":"0","pmts":[]}]}
#[{"app":"live","streams":[{"strm":"match","publish_time":"1557132035","bandwidth":"2603460","resolution":"720x576","vcodec":"avc1.4d401e","protocol":"MPEGTS"},{"strm":"5","publish_time":"1557132035","bandwidth":"2506175","resolution":"720x576","vcodec":"avc1.4d401e","protocol":"MPEGTS"}]}]

#['Cameras'][0]['st']

def monitoring_source():

    mpeg2ts_status = ((requests.get('http://192.168.1.247:8088/manage/mpeg2ts_status')).json())

    for obj in mpeg2ts_status['Cameras']:
    # Перебираем словарь и объекты.
    # Если ID объекта соответствует значению ключа ID словаря, присваиваем значение статуса объекту.
        for source in Source.objects.filter():
            if obj['id'] == str(source.pk):
                source.bitrate = round((int(obj['bw'])/1000000), 3)
                if obj['st'] == 'online':
                    source.status = True
                    #source.save()
                else:
                    source.status = False


                source.save()

def monitoring_outgoing():

    outgoing_status = ((requests.get('http://192.168.1.247:8088/manage/rtmp_status')).json())[0]

    for strm in outgoing_status['streams']:
        for stream in Stream.objects.filter():
            if strm['strm'] == stream.stream:
                try:
                    stream.bandwidth = round((int(strm['bandwidth'])/1000000), 3)
                except:
                    stream.bandwidth = 0
                stream.save()

def server_status():

    server_status = (requests.get('http://192.168.1.247:8088/manage/server_status').json())

    for server in Server.objects.filter():
        server.connection = server_status['Connections']
        server.outrate = server_status['OutRate']
        server.ap = server_status['SysInfo']['ap']
        server.scl = server_status['SysInfo']['scl']
        server.tpms = round((server_status['SysInfo']['tpms'])/1000000)
        server.fpms = round((server_status['SysInfo']['fpms'])/1000000)
        server.tsss = round((server_status['SysInfo']['tsss'])/1000000)
        server.fsss = round((server_status['SysInfo']['fsss'])/1000000)
        server.save()


