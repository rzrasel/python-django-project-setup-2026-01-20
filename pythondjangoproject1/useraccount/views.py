from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer
import traceback
from core.utilities.log_return import LogReturn
# Import ApiResponse
from core.response.api_response import ApiResponse

@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return ApiResponse.success(
        data=serializer.data,
        message="Users fetched successfully ",
        status=status.HTTP_200_OK,
        log=LogReturn.log(),
    )
    #return Response(UserSerializer({"name": "Rz Rasel", "age": 200}).data)

@api_view(['POST'])
def create_user(request):
    return _create_user_logic(request=request)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return ApiResponse.error(
            message="Data not found.",
            errors=serializer.errors,
            status=status.HTTP_404_NOT_FOUND,
            log=LogReturn.log(),
        )
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return ApiResponse.success(
            data=serializer.data,
            message="User found successfully.",
            status=status.HTTP_201_CREATED,
            log=LogReturn.log(),
        )
    elif request.method == 'POST':
        return _create_user_logic(request=request)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ApiResponse.success(
                data=serializer.data,
                message="User successfully saved.",
                status=status.HTTP_201_CREATED,
                log=LogReturn.log(),
            )
        return ApiResponse.error(
            data=request.data,
            message="User update error.",
            status=status.HTTP_400_BAD_REQUEST,
            errors=serializer.errors,
            log=LogReturn.log(),
        )
    elif request.method == 'DELETE':
        user.delete()
        return ApiResponse.success(
            data=request.data,
            message="User successfully deleted.",
            status=status.HTTP_204_NO_CONTENT,
            log=LogReturn.log(),
        )

def _create_user_logic(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return ApiResponse.success(
            data=serializer.data,
            message="User created successfully.",
            status=status.HTTP_201_CREATED,
            log=LogReturn.log(),
        )
    return ApiResponse.error(
        message="Validation failed.",
        errors=serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
        log=LogReturn.log(),
    )