from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from django.utils import timezone

@api_view(['GET'])
def health_check(request):
    """
    ヘルスチェックエンドポイント
    """
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)

class TodoViewSet(viewsets.ModelViewSet):
    """
    TodoのCRUD操作を行うためのViewSet
    """
    queryset = Todo.objects.filter(deleted_at__isnull=True)
    serializer_class = TodoSerializer

    def perform_destroy(self, instance):
        # 論理削除を行う
        instance.deleted_at = timezone.now()
        instance.save()
