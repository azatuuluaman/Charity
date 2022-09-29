from rest_framework import serializers
from .models import *


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = '__all__'


class DonationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    images = CategoryImageSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'images']


class DonationSerializer(serializers.ModelSerializer):
    article_images = DonationImageSerializer(many=True)

    class Meta:
        model = Donation
        fields = ['title', 'categoryId', 'description', 'target', 'progress', 'charityQty', 'city', 'owner',
                  'phone_number', 'creation_date', 'end_date', 'requisites', 'article_images']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = "__all__"

