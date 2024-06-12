from rest_framework import serializers
from chat.models import ChatRoom, Message

class ChatRoomSerializer(serializers.ModelSerializer):
    # serializers define a format of input and output 
    class Meta:
        model = ChatRoom
        fields = ["id", "name"]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "text", "chat_room", "user"]