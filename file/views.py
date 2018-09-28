from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view


class FileView(APIView):
    """
        METHOD : POST,form-data
        파라미터
        file_key
        file_name
        file_path
        user_id
        project
        expire_min

    METHOD : GET
        /file/file_key/ : /file/1/
    """

    parser_classes = (MultiPartParser,)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):

        file_path = request.data.get('file_path')

        if file_path is None:
            return Response({
                "result": -1,
                "message": '이미지 데이터가 없습니다.'
            }, status=status.HTTP_400_BAD_REQUEST)

        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response({
                "result": 1,
                "message": 'success',
                "data": file_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "result": 0,
                "message":  file_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, file_key, format=None):
        try:
            file = File.objects.get(file_key=file_key)
            serializer = self.serializer_class(file)
            return Response({
                "result": 1,
                "message": 'found',
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except File.DoesNotExist:
            return Response({
                "result": 0,
                "message": 'not found'
            }, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def delete(request):
    """
    삭제
    보낼 데이터는 다음과 같습니다.
    post:
    삭제

    """
    try:
        file = File.objects.get(file_key=request.data.get("file_key"))
        file.delete()

        return Response({
            "result": 1,
            "message": 'success'
        }, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response({
            "result": 0,
            "message": 'not found'
        }, status=status.HTTP_404_NOT_FOUND)