# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModelA
from .serializers import ModelASerializer
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser


class ModelAListView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def get(self, request, *args, **kwargs):
        model_a_instances = ModelA.objects.all()
        serializer = ModelASerializer(model_a_instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ModelASerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
