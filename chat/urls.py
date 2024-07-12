from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chat.views import sumNumbersView
from chat.viewsets import ChatRoomViewSet, MessageViewSet

#here is the problem
router = DefaultRouter()
router.register(r'chatroom', ChatRoomViewSet, basename='chatroom')
router.register(r'message', MessageViewSet, basename='message')
urlpatterns = router.urls
urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
    # path('register/', register, name='register'),
]
