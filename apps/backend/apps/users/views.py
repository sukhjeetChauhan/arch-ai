from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import User

# User Views

# get Users
@api_view(['GET'])
def get_all_Users():
  users = User.objects.all()
  serializer = UserSerializer(users, many = True)
  return Response(serializer.data)




