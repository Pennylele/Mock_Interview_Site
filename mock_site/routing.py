from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/session/<uuid>/', consumers.ChatConsumer.as_asgi()),
]
