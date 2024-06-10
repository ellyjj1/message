from rest_framework import serializers
from chat.models import ChatRoom

class ChatRoomSerializer(serializers.ModelSerializer):
    # serializers define a formate of input and output 
    class Meta:
        model = ChatRoom
        fields = ["id", "name"]