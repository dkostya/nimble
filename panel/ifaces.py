import netifaces
from .models import Iface

ifaces = {}
ifaces_name = netifaces.interfaces()
ifaces_ip = []


for name in ifaces_name:

    try:
        addresses = netifaces.ifaddresses(name).get(2)
        ifaces_ip.append(str(addresses[0]['addr']))

    except:
        print('IP адреса определить не удалось')

print(ifaces_ip)

iplist = [Iface for i in range(len(ifaces_ip)-1)]
for obj in iplist:
    try:
        for ip in ifaces_ip:
            obj = Iface(iface_ip=ip)
            obj.save()
    except:
        print('такой IP уже есть')




print(iplist)



