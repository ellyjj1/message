from django.test import TestCase

# Create your tests here.
# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ChatRoom
from .serializers import ChatRoomSerializer

class ChatRoomViewSetTest(APITestCase):
    def setUp(self):
        # 创建一些测试数据
        self.chat_room1 = ChatRoom.objects.create(name='Room 1')
        self.chat_room2 = ChatRoom.objects.create(name='Room 2')
        self.valid_payload = {'name': 'New Room'}
        self.invalid_payload = {'name': ''}

    def test_get_all_chatrooms(self):
        response = self.client.get(reverse('chatroom-list'))
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_chatroom(self):
        response = self.client.post(reverse('chatroom-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_chatroom(self):
        response = self.client.post(reverse('chatroom-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_valid_single_chatroom(self):
        response = self.client.get(reverse('chatroom-detail', kwargs={'pk': self.chat_room1.pk}))
        chatroom = ChatRoom.objects.get(pk=self.chat_room1.pk)
        serializer = ChatRoomSerializer(chatroom)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_chatroom(self):
        response = self.client.put(reverse('chatroom-detail', kwargs={'pk': self.chat_room1.pk}),
                                   data={'name': 'Updated Room'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Room')

    def test_delete_chatroom(self):
        response = self.client.delete(reverse('chatroom-detail', kwargs={'pk': self.chat_room1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ChatRoom.objects.filter(pk=self.chat_room1.pk).exists())
