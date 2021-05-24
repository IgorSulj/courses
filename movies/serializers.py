from django.urls import reverse
from rest_framework.serializers import *
from .models import Movie, ProductModel, CountryModel


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1

    def create(self, validated_data=None):
        validated_data = validated_data or self.validated_data
        movie = Movie(**validated_data)
        return movie

    def update(self, instance=None, validated_data=None):
        instance = instance or self.instance
        validated_data = validated_data or self.validated_data
        instance.title = validated_data.get('title', instance.title)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        # instance.save()
        return instance


class CountrySerializer(ModelSerializer):

    class Meta:
        model = CountryModel
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    made_in = CountrySerializer(many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'

    def create(self, validated_data):
        countries = validated_data.pop('made_in')
        product = ProductModel.objects.create(**validated_data)
        db_countries = []
        for country in countries:
            db_country = CountryModel.objects.get_or_create(name=country.get('name'),
                                                            political_system=country.get('political_system'))[0]
            db_countries.append(db_country.pk)
        product.made_in.set(db_countries)
        product.save()
        return product



