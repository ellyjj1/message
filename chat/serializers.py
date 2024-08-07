from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import ChatRoom, Message

class ChatRoomSerializer(serializers.ModelSerializer):
    # serializers define a format of input and output 
    class Meta:
        model = ChatRoom
        fields = ["id", "name", "created_by", "members"]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "text", "chat_room", "user"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']