from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_nested_routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Initialize the main router
router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Initialize the nested router
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Define the URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(nested_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
]
