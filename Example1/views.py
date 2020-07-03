from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

from django.http import Http404
from django.shortcuts import get_object_or_404

#exportacion de serializer y modelos 
from Example1.models import Example1
from Example1.serializer import ExampleSerializers

class ExampleLista(APIView):
    def get(self,request,format=None):
        print("ENTRAMOS A GET OSI OSI")
        queryset = Example1.objects.all()
        serializer = ExampleSerializers(queryset,many = True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = ExampleSerializers(data = request.data)
        print("PASAMOS SERIALIZER Y ENTRAMOS A POST")
        if serializer.is_valid():
            print("ENTRAMOS AL IF")
            serializer.save()
            datas = serializer.data
            return Response(datas)