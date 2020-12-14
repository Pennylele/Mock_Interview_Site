"""
ASGI config for django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
# os.environ['DJANGO_SETTINGS_MODULE'] = "django.settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import mock_site.routing
from channels.routing import get_default_application
import django

application = get_default_application()
django.setup()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             mock_site.routing.websocket_urlpatterns
#         )
#     ),
# })