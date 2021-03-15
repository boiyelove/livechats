"""
ASGI config for livechats project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chats.routing import websocket_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livechats.settings')
# application = get_asgi_application()
application = ProtocolTypeRouter({
	"websocket": AuthMiddlewareStack(
		URLRouter(
			)
		)
	})
