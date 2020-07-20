from django.urls import path, include
from .views import ListCreateItemView, RetrieveUpdateDeleteItemView, \
    CreateBuyerInterest
urlpatterns = [
    path('store/<item_id>/interested/', CreateBuyerInterest.as_view(), name='buyer-create-interest'),
    path('store/<item_id>/', RetrieveUpdateDeleteItemView.as_view(), name='item-retrieve-delete'),
    path('store/', ListCreateItemView.as_view(), name='item-list'),
]