from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView
from users.models import Profile
from users.serialazers import ProfileSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileDetailApi(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_class = [IsAuthenticated,]

    def get(self,request,*args,**kwargs):
        data = {"message":"Hello world"}
        return Response(data)
# Create your views here.
