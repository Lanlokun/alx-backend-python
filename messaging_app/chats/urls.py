from django.urls import path, include
from rest_framework import routers

from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Define the URL patterns
urlpatterns = [
    path("api/", include(router.urls))
]
