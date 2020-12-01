from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/mock_site/(?P<uuid>\w+)/$', consumers.ChatConsumer.as_asgi()),
]