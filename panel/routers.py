from rest_framework import routers
from panel.viewsets import SourceViewSet, StreamViewSet, IfaceViewSet, \
    RtmpSettingsViewSet, ProtocolsViewSet, ABRstreamViewSet, ServerViewSet


router = routers.DefaultRouter()
router.register(r'sources', SourceViewSet)
router.register(r'streams', StreamViewSet)
router.register(r'ifaces', IfaceViewSet)
router.register(r'rtmpsettings', RtmpSettingsViewSet)
router.register(r'protocols', ProtocolsViewSet)
router.register(r'abrstreams', ABRstreamViewSet)
router.register(r'server', ServerViewSet)
