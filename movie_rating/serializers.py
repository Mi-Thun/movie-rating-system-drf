from rest_framework import serializers
from .models import User, Movie, Rating
from django.db.models import Avg

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'email', 'password']

from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)
        
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class MovieSerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__' 

    def get_average_rating(self, obj):
        return Rating.objects.filter(movie_id=obj).aggregate(Avg('rating'))['rating__avg']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
