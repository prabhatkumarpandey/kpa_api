from django.shortcuts import render
# formapi/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserData
from .serializers import UserDataSerializer

class AddUser(APIView):
    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User added", "data": serializer.data}, status=201)
        return Response(serializer.errors, status=400)

class GetUsers(APIView):
    def get(self, request):
        users = UserData.objects.all()
        serializer = UserDataSerializer(users, many=True)
        return Response(serializer.data)

# Create your views here.
