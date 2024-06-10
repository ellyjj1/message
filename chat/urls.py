from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSet

router = DefaultRouter()

router.register( r'chatroom', ChatRoomViewSet, basename='chatroom')
urlpatterns = router.urls