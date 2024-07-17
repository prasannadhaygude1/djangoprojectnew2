

from django.shortcuts import render,HttpResponse

from .models import client,Project
from .serializers import clientserializer,ProjectSerializer
from rest_framework.renderers import JSONRenderer

import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return render(request,"home.html")

def clientdetails(request,id):
    s = client.objects.get(id=id)
    serializer = clientserializer(s)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

def client_list(request):
    cl=client.objects.all()
    serializer = clientserializer(cl ,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")

def projectdetails(request,id):
    p = Project.objects.get(id=id)
    serializer = ProjectSerializer(p)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")


@csrf_exempt
def client_create(request):
    if request.method=="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = clientserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def project_create(request):
    if request.method=="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ProjectSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

def project_details(request):
    p = Project.objects.all()
    serializer = ProjectSerializer(p,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")