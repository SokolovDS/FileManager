from rest_framework import generics

from file_manager.models import File
from file_manager.serializers import FileSerializer


class SaveFileView(generics.CreateAPIView):
    serializer_class = FileSerializer


class AllFilesView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
