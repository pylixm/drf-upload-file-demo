# -*- coding:utf-8 -*-
from PIL import Image
from rest_framework import viewsets, status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from uploaddemo.models import Airticle
from .serializers import AirticleSerializer, AirticlePicSerializer


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


class AirticleViewSet(viewsets.ModelViewSet):
    queryset = Airticle.objects.all()
    serializer_class = AirticleSerializer

    @action(methods=['put'], detail=True, serializer_class=AirticlePicSerializer,
            parser_classes=[MultiPartParser])
    def upload(self,  request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)


class ImageUploadView(APIView):

    parser_class = (ImageUploadParser,)

    def put(self, request, filename, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        try:
            img = Image.open(f)
            img.verify()
        except:
            raise ParseError("Unsupported image type")

        airticle = Airticle()
        airticle.image.save(filename if filename else f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)