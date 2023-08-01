from django.conf import settings
from rest_framework.response import Response
from .serializers import user_data_serializer
from rest_framework import viewsets

members_data =settings.DB['user_data']


class ListUsers(viewsets.ViewSet):
    def list(self,request):
        queryset = members_data.find()
        serializer = user_data_serializer(queryset,many = True)
        return Response(serializer.data)

    def create(self,request):
        serializer=user_data_serializer(data=request.data)
        if serializer.is_valid():
            members_data.insert_one(serializer.data)
        return Response(serializer.data)
