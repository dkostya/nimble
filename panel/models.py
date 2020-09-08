from django.db import models



# Create your models here.

class Iface(models.Model):

    iface_ip = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.iface_ip

class Source(models.Model):

    PROTOCOLS = (
        ('udp', 'udp'),
        ('http', 'http'),
        ('rtp', 'rtp')
    )


    status = models.BooleanField(default=False)
    bitrate = models.FloatField(default=0, verbose_name='bitrate')
    name = models.CharField(max_length=24, verbose_name='Имя потока', blank=True)
    ip = models.GenericIPAddressField(verbose_name='Мультикаст IP')
    port = models.IntegerField(default=1234, verbose_name='Мультикаст порт')
    miface = models.ForeignKey(Iface, to_field='iface_ip', on_delete=models.PROTECT)
    protocol = models.CharField(max_length=8, choices=PROTOCOLS, default='udp')

    def __str__(self):
        return '%s %s:%s' % (self.name, self.ip, self.port)


class Stream(models.Model):

    video = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, related_name='video')
    vpid = models.IntegerField(null=True)

    audio = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, related_name='audio')
    apid = models.IntegerField(null=True)

    app = models.CharField(max_length=20, default='live')
    stream = models.CharField(max_length=20)

    bandwidth = models.FloatField(default=0, verbose_name='bandwidth')

    def __str__(self):
        return '%s' % (self.id)


class Protocols(models.Model):
    PROTOCOLS = (
        ('HLS', 'HLS'),
        ('RTMP', 'RTMP'),
        ('DASH', 'DASH'),
        ('RTSP', 'RTSP')
    )

    protocol = models.CharField(unique=True, choices=PROTOCOLS, max_length=16)

    def __str__(self):
        return '%s' % (self.protocol)

class ABRSource(models.Model):

    app = models.CharField(max_length=24, null=True)
    stream = models.CharField(max_length=24, null=True)

class ABRStream(models.Model):

    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=24, blank=True, null=True)
    stream = models.CharField(max_length=24, blank=True, null=True)
    order = models.CharField(max_length=24, default="DESC")
    streams = models.ManyToManyField(ABRSource)

class RtmpSettings(models.Model):

    hash = models.CharField(max_length=24, default="1", blank=True, null=True)
    interfaces = []
    login = models.CharField(max_length=24, default="", blank=True, null=True)
    password = models.CharField(max_length=24, default="", blank=True, null=True)
    duration = models.IntegerField(null=True)
    chunk_count = models.IntegerField(null=True)
    dash_template = "TIME"
    apps = []
    protocols = models.ManyToManyField(Protocols)

class Server(models.Model):

    servername = models.CharField(max_length=24, default='servername', blank=True, null=True)
    connection = models.IntegerField(null=True)
    outrate = models.FloatField(null=True)
    ap = models.IntegerField(null=True)
    scl = models.FloatField(null=True)
    tpms = models.BigIntegerField(null=True)
    fpms = models.BigIntegerField(null=True)
    tsss = models.BigIntegerField(null=True)
    fsss = models.BigIntegerField(null=True)

    def __str__(self):
        return self.servername
