from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import createUser

# Create your views here.
@api_view(['POST'])
def createUsers(request):
    data = {} 
    user = UserSerializer(data = request.data)
    user.is_valid(raise_exception=True)
    user.save()
    data['data'] = "User created Successfully"
    return Response(data, status.HTTP_200_OK)

@api_view(['GET'])
def getUser(request):
    userdata = createUser.objects.all()
    user = UserSerializer(userdata, many=True)

    return Response(user.data, status.HTTP_200_OK)

@api_view(['POST'])
def deleteUser(request):
    data = {}
    getId = request.data.get('id')
    try:
        userdata = createUser.objects.get(id = getId).delete()
    except createUser.DoesNotExist:
        data['data'] = "User Not Found"
        return Response(data, status.HTTP_200_OK)
    except:
        data['data'] = "Something is not found"
        return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)

    data['data'] = "User deleted Successfully"
    return Response(data, status.HTTP_200_OK)


@api_view(['POST'])
def updateUser(request):
    data = {}
    getID = request.data.get('id')
    try:
        userdetails = createUser.objects.get(id = getID)
    except createUser.DoesNotExist:
        data['data'] = "User does not Exists"
        return Response(data, status.HTTP_200_OK)
    except:
        data['data'] = "something went wrong"
        return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)

    user = UserSerializer(userdetails, data = request.data)
    user.is_valid(raise_exception=True)
    user.save()
    data['data'] = "User Updated Successfully"
    return Response(data, status.HTTP_200_OK)