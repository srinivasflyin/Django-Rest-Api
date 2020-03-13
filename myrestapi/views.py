from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import (HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_401_UNAUTHORIZED,HTTP_403_FORBIDDEN)
from rest_framework.response import Response
from .token import generate_accesstoken, generate_refreshtoken
from .models import User
from datetime import datetime
import random
from django.contrib.auth import hashers
# Create your views here.


# @csrf_exempt
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     if (username is None or password is None):
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username,password=password)
#     if(not user):
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)
#@permission_classes((IsAuthenticated),)
# def getuserdetails:
#     user =

#
@csrf_exempt
@api_view(['POST'])
def login(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    if(request.data and username and password):
        try:
            user = User.objects.get(username= username)
            if(user):
                tokens = generate_accesstoken({'username': username, 'password': password, id: user.id});
        except:
            print('Exception is occured')
            return Response({'message': 'something went wrong'},status=HTTP_404_NOT_FOUND)
    else:
        return Response({'message': 'something went wrong'}, status=HTTP_404_NOT_FOUND)
def generateRefreshToken(request):
    if (request.body.refreshtoken):
        tokens = generate_refreshtoken(request.data.refreshtoken)
        return Response(tokens,status=HTTP_200_OK)
    else:
        return Response({'message': 'Invalid token'}, status=HTTP_401_UNAUTHORIZED)
@csrf_exempt
@api_view(['POST'])
def createUser(request):
    try:
        user =  User.objects.get(firstName= request.data.get('firstName'))
        if(user):
            user.lastName = request.data.get('lastName');
            user.firstName = request.data.get('firstName');
            user.created_at = datetime.now().date();
            user.updated_at = datetime.now().date();
    except ObjectDoesNotExist:
        user = User();
        user.firstName = request.data.get('firstName');
        user.lastName = request.data.get('lastName');
        user.updated_at = datetime.now().date();
        pwd = hashers.make_password('srinivas',salt=None,hasher='default')
        print('pwd=============', pwd)
       # password = hashers.make_password(request.data.get('password'),salt=None, hasher=hashers.PBKDF2PasswordHasher)
    #user.save()
    return Response({'messge': 'usercreated successfylly'}, status=HTTP_200_OK);