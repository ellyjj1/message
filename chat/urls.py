from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSet, MessageViewSet

router = DefaultRouter()
router.register( r'chatroom', ChatRoomViewSet, basename='chatroom')
router.register( r'message', MessageViewSet, basename='message')
urlpatterns = router.urls

