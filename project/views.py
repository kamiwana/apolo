from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
''
class ProjectView(APIView):
    """
        METHOD : POST, form-data
        파라미터
        project_key
        project_name
        global_variables

    METHOD : GET
        /project/project_key/ : /project/1/
    """

    serializer_class = ProjectSerializer

    def post(self, request, *args, **kwargs):

        Project_serializer = self.serializer_class(data=request.data)
        if Project_serializer.is_valid():
            Project_serializer.save()

            return Response({
                "result": 1,
                "message": 'success',
                "data": Project_serializer.data
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "result": 0,
                "message": 'fail',
                "data": Project_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, project_key, format=None):
        try:
            project = Project.objects.get(project_key=project_key)
            serializer = self.serializer_class(project)
            return Response({
                "result": 1,
                "message": 'success',
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Project.DoesNotExist:
            return Response({
                "result": 0,
                "message": 'fail'
            }, status=status.HTTP_404_NOT_FOUND)