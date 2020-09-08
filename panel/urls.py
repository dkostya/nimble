from django.urls import path, include
from django.conf.urls import url
from panel import views
from .routers import router
from .ifaces import iplist


urlpatterns = [

    path('', views.IndexView.as_view(), name = 'index'),

#Здесь записываю конфигурацию в конфиг нимбла
    url('write_config/', views.write_config, name = 'write_config'),

#URL источников
    path('sources/', views.SourcesList.as_view(), name = 'sources_list'),
    path('sources/<int:pk>', views.SourceDetail.as_view(), name='source_detail'),
    path('source/create', views.SourceCreate.as_view(), name='source_create'),
    path('source/update/<int:pk>', views.SourceUpdate.as_view(), name='source_update'),
    path('source/delete/<int:pk>', views.SourceDelete.as_view(), name='source_delete'),

#Исходящих потоков
    path('streams/', views.StreamsList.as_view(), name='streams_list'),
    path('streams/<int:pk>', views.StreamDetail.as_view(), name='stream_detail'),
    path('stream/create', views.StreamCreate.as_view(), name='stream_create'),
    path('stream/update/<int:pk>', views.StreamUpdate.as_view(), name='stream_update'),
    path('stream/delete/<int:pk>', views.StreamDelete.as_view(), name='stream_delete'),

#DRF API

    path('api/', include(router.urls)),
    path('api/rest-auth/', include('rest_auth.urls'))

]
