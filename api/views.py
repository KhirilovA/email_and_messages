from rest_framework import viewsets

from api.models import Message
from api.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.none()

class MessageListViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = MessageSerializer
	queryset = Message.objects.all()

class SingleMessageViewSet(viewsets.ModelViewSet):
	serializer_class = MessageSerializer
	queryset = Message.objects.all()