import sys
import os
import django
import requests

sys.path.append("/home/user/myproject/nimble/")

# Request example:

# curl -vvv http://127.0.0.1:8082/manage/mpeg2ts_status
# Response example:
# {"Cameras":[{"id":"1","st":"offline","tr":"0","bw":"0","pmts":[]},{"id":"2","st":"offline","tr":"0","bw":"0","pmts":[]}]}

#['Cameras'][0]['st']

def monitoring():
    from panel.models import Source
    mpeg2ts_status = ((requests.get('http://192.168.1.247:8088/manage/mpeg2ts_status')).json())



    for obj in mpeg2ts_status['Cameras']:
    # Перебираем словарь и объекты.
    # Если ID объекта соответствует значению ключа ID словаря, присваиваем значение статуса объекту.
        for source in Source.objects.filter():
            if int(obj['id']) == source.pk:
                source.bitrate = round((int(obj['bw'])/1000000), 3)
                if obj['st'] == 'online':
                    source.status = True
                    #source.save()
                else:
                    source.status = False
                    #source.save()

                source.save()



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nimble.settings")
    django.setup()
    monitoring()


