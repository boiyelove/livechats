"""
ASGI config for livechats project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddleWareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chats.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livechats.settings')

print('now in asgi')
# application = get_asgi_application()
application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	"websocket" : AuthMiddleWareStack(
		URLRouter(
			chats.routing.websocket_urlpatterns
			)
		),
	})


