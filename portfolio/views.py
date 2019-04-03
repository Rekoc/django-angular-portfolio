from portfolio.serializers import PortfolioItemSerializer, PortfolioItemSmallSerializer
from portfolio.models import PortfolioItem
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all().order_by('-creation_date')
    serializer_class = PortfolioItemSerializer

    # When listing we will use PortfolioItemSmallSerializer instead of PortfolioItemSerializer
    # to reduce the number of data sent
    def list(self, request, *args, **kwargs):
        list_item = PortfolioItem.objects.all().order_by('-date_creation')
        serializer = PortfolioItemSmallSerializer(list_item, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def list_item(request):
    if request.method == 'GET':
        item_list = PortfolioItem.objects.all()
        serializer = PortfolioItemSerializer(item_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PortfolioItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def items_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        item_list = PortfolioItem.objects.get(pk=pk)
    except PortfolioItem.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PortfolioItemSerializer(item_list)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PortfolioItemSerializer(item_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item_list.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
