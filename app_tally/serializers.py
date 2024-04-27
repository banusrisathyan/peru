from rest_framework import serializers
from .models import Product,BreastfeedingDetail,PoopDetail,UserInfo


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BreastfeedingDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BreastfeedingDetail
        fields = '__all__'

class PoopDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoopDetail
        fields = '__all__'




class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [ 'name', 'date_of_birth', 'pregnant']