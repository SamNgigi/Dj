# from django.shortcuts import render
# from django.http import (
#     HttpResponse,
#     # JsonResponse
# )
from django.http import Http404
# from django.views.decorators.csrf import csrf_exempt

from .models import ApiTest
from .serializers import ApiTestSerializer

from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


"""
Class based execution
"""


class ApiTestList(APIView):
    """
    Lists all the test apis list, or create a new snippet
    """

    def get(self, request, format=None):
        api_test = ApiTest.objects.all()
        apiSerializer = ApiTestSerializer(api_test, many=True)
        return Response(apiSerializer.data)

    def post(self, request, format=None):
        apiSerializer = ApiTestSerializer(data=request.data)
        if apiSerializer.is_valid():
            apiSerializer.save()
            return Response(apiSerializer.data, status=status.HTTP_201_CREATED)
        return Response(
            apiSerializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ApiTestDetails(APIView):
    """
    Retrieve, update or delete a snippet instance
    """

    def get_object(self, pk):
        try:
            return ApiTest.objects.get(pk=pk)
        except ApiTest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        api_test = self.get_object(pk)
        apiSerializer = ApiTestSerializer(api_test)
        return Response(apiSerializer.data)

    def put(self, request, pk, format=None):
        api_test = self.get_object(pk)
        apiSerializer = ApiTestSerializer(api_test, data=request.data)
        if apiSerializer.is_valid():
            apiSerializer.save()
            return Response(apiSerializer.data)
        return Response(
            apiSerializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        api_test = self.get_object(pk)
        api_test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response('Success!')
    # def list(self, request):
    #     api_test = ApiTest.objects.all()
    #     apiSerializer = ApiTestSerializer(api_test, many=True)
    #     return Response(apiSerializer.data)
    #
    # def retrieve(self, request, pk):
    #     api_test = ApiTest.objects.get_object_or_404(pk=pk)
    #     apiSerializer = ApiTestSerializer(api_test)
    #     return Response(apiSerializer.data)

        # pass


"""
Function based views execution.

# @csrf_exempt
@api_view(['GET', 'POST'])
def api_list(request, format=None):

    # List all code apiTests, or create new

    if request.method == 'GET':
        api_test = ApiTest.objects.all()
        apiSerializer = ApiTestSerializer(api_test, many=True)
        return Response(apiSerializer.data)
    elif request.method == 'POST':
        apiSerializer = ApiTestSerializer(data=request.data)
        if apiSerializer.is_valid():
            apiSerializer.save()
            return Response(apiSerializer.data, status=status.HTTP_201_CREATED)
        return Response(
            apiSerializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk, format=None):

    # Retrieve, update or delele a code snippet.

    try:
        api_test = ApiTest.objects.get(pk=pk)
    except ApiTest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        apiSerializer = ApiTestSerializer(api_test)
        return Response(apiSerializer.data)
    elif request.method == 'PUT':
        apiSerializer = ApiTestSerializer(apiSerializer, data=request.data)
        if apiSerializer.is_valid():
            apiSerializer.save()
            return Response(apiSerializer.data)
        return Response(
            apiSerializer.error,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        apiSerializer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response('Success!')
        # pass


"""
