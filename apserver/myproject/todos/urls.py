from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, health_check

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('', include(router.urls)),
]
