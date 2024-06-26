from django.shortcuts import render
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = [AllowAny]
  serializer_class = UserRegisterSerializer


from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'message': "Login Successful", 'isLogin': True, 'refresh_token': str(refresh), 'access_token': str(refresh.access_token)})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutAPIView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            print("Received refresh token:", refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("Logout Successful", status=status.HTTP_200_OK)
        except KeyError:
            return Response("Refresh token not provided", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("An error occurred: " + str(e), status=status.HTTP_400_BAD_REQUEST)
           



class UserDetailAPI(APIView):
  def get(self,request,*args,**kwargs):

    user = User.objects.get(id=request.user.id)
    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
       return Response("No Such User")