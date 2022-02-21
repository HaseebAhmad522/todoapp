import re
from sys import api_version
from unicodedata import name
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import InformationSerializer
from app.models import Information
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse


class informationviewset(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     api_data = self.queryset.filter(name='Sufiyan')
    #     api = {'api_data': api_data}
    #     serializer = InformationSerializer(data=api)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    # api_data = self.queryset.filter(name='Sufiyan')
    # return reverse('api-detail', kwargs={"pk": api_data})
