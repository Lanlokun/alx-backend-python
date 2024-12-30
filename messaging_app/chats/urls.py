from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Define the URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # Prefixing all the URLs with /api/
]
