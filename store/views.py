from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .serializers import ItemSerialiazer, BuyerSerializer
from .models import ORMItem, ORMBuyer
# Create your views here.

class ListCreateItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ItemSerialiazer
    queryset = ORMItem.objects.filter(is_sold=False)


class RetrieveUpdateDeleteItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ItemSerialiazer
    queryset = ORMItem.objects.all()
    http_method_names = ['get', 'patch', 'delete']
    lookup_field = 'item_id'


class CreateBuyerInterest(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuyerSerializer
    queryset = ORMBuyer.objects.all()
    lookup_url_kwarg = 'item_id'

    def post(self, request, *args, **kwargs):

        print('### ', request.data)
        item_id = self.kwargs.get(self.lookup_url_kwarg)
        item = ORMItem.objects.get(item_id=item_id)
        
        request.data['item'] = item.pk
        return super().post(request, *args, **kwargs)

