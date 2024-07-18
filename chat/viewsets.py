from django.contrib.auth.models import User
from rest_framework import viewsets
from chat.models import ChatRoom, Message
from chat.serializers import ChatRoomSerializer, MessageSerializer, UserSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
