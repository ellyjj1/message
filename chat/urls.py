from django.urls import path, include
from rest_framework.routers import DefaultRouter

from chat.views import sumNumbersView
from chat.viewsets import ChatRoomViewSet, MessageViewSet, UserViewSet

router = DefaultRouter()
router.register(r'chatroom', ChatRoomViewSet, basename='chatroom')
router.register(r'message', MessageViewSet, basename='message')
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
    # path('register/', register, name='register'),
]
