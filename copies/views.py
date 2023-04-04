from rest_framework.generics import ListAPIView
from .models import Copy
from .serializers import CopyListSerializer

class CopyList(ListAPIView):
    serializer_class = CopyListSerializer

    def get_queryset(self):
        return Copy.objects.all()
