from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, BreastfeedingDetail,PoopDetail,UserInfo
from .serializers import ProductSerializer, BreastfeedingDetailSerializer,PoopDetailSerializer,UserInfoSerializer
from django.shortcuts import render
from django.http import JsonResponse





class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BreastfeedingDetailView(viewsets.ModelViewSet):
    queryset = BreastfeedingDetail.objects.all()
    serializer_class = BreastfeedingDetailSerializer

class PoopDetailView(viewsets.ModelViewSet):
     queryset = PoopDetail.objects.all()
     serializer_class = PoopDetailSerializer



from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User information saved successfully'}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
