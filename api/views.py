# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import ApiTest
from .serializers import ApiTestSerializer

from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


@csrf_exempt
def api_list(request):
    """
    List all code apiTests, or create new
    """
    if request.method == 'GET':
        api_test = ApiTest.objects.all()
        apiSerializer = ApiTestSerializer(api_test, many=True)
        return JsonResponse(apiSerializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        apiSerializer = ApiTestSerializer(data=data)
        if apiSerializer.is_valid():
            apiSerializer.save()
            return JsonResponse(apiSerializer.data, status=201)
        return JsonResponse(apiSerializer.errors, status=400)


@csrf_exempt
def api_detail(request, pk):
    """
    Retrieve, update or delele a code snippet.
    """
    try:
        api_test = ApiTest.objects.get(pk=pk)
    except ApiTest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        apiSerializer = ApiTestSerializer(api_test)
        return JsonResponse(apiSerializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        apiSerializer = ApiTestSerializer(data=data)
        if apiSerializer.is_valid():
            apiSerializer.save()
            return JsonResponse(apiSerializer.data)
        return JsonResponse(apiSerializer.error, status=400)

    elif request.method == 'DELETE':
        apiSerializer.delete()
        return HttpResponse(status=204)


class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response('Success!')
        # pass
