from django.conf.urls import url

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from ABC.messager.consumers import MessagerConsumer
from ABC.notifications.consumers import NotificationsConsumer

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r'^notifications/$', NotificationsConsumer),
                url(r'^(?P<username>[^/]+)/$', MessagerConsumer),
            ])
        ),
    ),
})
