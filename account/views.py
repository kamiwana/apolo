from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.schemas import AutoSchema

@api_view(["POST"])
def login(request):
    """
    로그인
    보낼 데이터는 다음과 같습니다.
    post:
    로그인
    user_id
    password
    project
    """
    project = request.data.get("project")
    user_id = request.data.get("user_id")
    password = request.data.get("password")

    try:
        user = User.objects.get(user_id=user_id, project=project)

        if user.check_password(password):
            data = {"result":1,
                    "message":"success",
                    "user_name": user.user_name,
                    "user": user.id
                 }
            return Response(data,status=status.HTTP_200_OK)
        else:
            data = {
                "result": -1,
                "message": '패스워드가 다릅니다.',
            }
            return Response(data,status=status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        data = {
            "result": -1,
            "message": '등록된 정보가 없습니다.',
        }
        return Response(data,status=status.HTTP_404_NOT_FOUND)

from rest_framework.generics import CreateAPIView
# Create your views here.
class UserView(CreateAPIView):
    serializer_class = AccountSerializer

    def post(self, request):

        project_key = self.request.data.get("project")
        user_id = self.request.data.get("user_id")
        try:
            my_object = User.objects.get(user_id=user_id,project=project_key)
            return Response({
                "result": -1,
                "message": 'already-아이디가 이미 존재합니다.',
            }, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:

            data = request.data.copy()
            data["user_key"] = project_key + "_" + user_id

            #try:
            #   my_object = Project.objects.get(project_key=project_key)
            #except Project.DoesNotExist:
            #    return Response({
            #        "result": 0,
            #        "message": 'fail - 프로젝트 키가 존재하지 않습니다.',
            #    }, status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():

                user = serializer.save()
                user.set_password(user.password)
                user.save()

                if user:
                    return Response({
                        "result": 1,
                        "message": 'success',
                        "data": data
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "result": 0,
                    "message":  serializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def get(request):
        project = request.data.get("project")
        user_id = request.data.get("user_id")
        password = request.data.get("password")

        try:
            user = User.objects.get(user_id=user_id, project=project)
            serializer = AccountSerializer(user)

            if user.check_password(password):
                return Response({
                    "result": 1,
                    "message": 'found',
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                data = {
                    "result": -1,
                    "message": '패스워드가 다릅니다.',
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({
                "result": 0,
                "message": 'not found'
            }, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def set(request):
    project = request.data.get("project")
    user_id = request.data.get("user_id")

    try:
        user = User.objects.get(user_id=user_id, project=project)
    except User.DoesNotExist:
        return Response({
            "result": 0,
            "message": 'not found'
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = AccountUpdateSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({
            "result": 1,
            "message": 'success'
        }, status=status.HTTP_200_OK)

    return Response({
        "result": 0,
        "message": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def delete(request):
    """
    탈퇴
    보낼 데이터는 다음과 같습니다.
    post:
    탈퇴
    user_id,project
    """
    try:
        user = User.objects.get(user_id=request.data.get("user_id"), project=request.data.get("project"))
        user.delete()

        return Response({
            "result": 1,
            "message": 'success'
        }, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response({
            "result": 0,
            "message": 'not found'
        }, status=status.HTTP_404_NOT_FOUND)