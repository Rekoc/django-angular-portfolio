from rest_framework import serializers
from portfolio.models import ImageField, PortfolioItem


class ImageFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageField
        fields = ('id', 'image', 'title', 'sub_title')


class PortfolioItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = ('id', 'title', 'is_displayed', 'view', 'description', 'image1', 'image2', 'image3')


class PortfolioItemSmallSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = ('id', 'title', 'is_displayed', 'image1')
