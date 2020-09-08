from django.contrib import admin
from .models import Source, Stream, Iface, RtmpSettings, Protocols, ABRStream, ABRSource, Server

# Register your models here.

class SourcesAdmin(admin.ModelAdmin):
    list_display = ('status', 'pk', 'id', 'ip', 'port', 'miface', 'protocol')

class StreamsAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'vpid', 'audio', 'apid', 'app', 'stream')

class IfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'iface_ip')

class RtmpSettingsAdmin(admin.ModelAdmin):
    list_display = ('hash', 'interfaces', 'login', 'password', 'duration', 'chunk_count', 'dash_template',
                    'apps')

class ProtocolsAdmin(admin.ModelAdmin):
    pass

class ABRStreamAdmin(admin.ModelAdmin):
    pass

class ABRSourceAdmin(admin.ModelAdmin):
    pass

class ServerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Source, SourcesAdmin)
admin.site.register(Stream, StreamsAdmin)
admin.site.register(Iface, IfaceAdmin)
admin.site.register(RtmpSettings, RtmpSettingsAdmin)
admin.site.register(Protocols, ProtocolsAdmin)
admin.site.register(ABRStream, ABRStreamAdmin)
admin.site.register(ABRSource, ABRSourceAdmin)
admin.site.register(Server, ServerAdmin)


