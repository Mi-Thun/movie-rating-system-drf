from rest_framework import serializers
from .models import User, Movie, Rating
from django.db.models import Avg

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone', 'email', 'password']

class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__' 

    def get_average_rating(self, obj):
        return Rating.objects.filter(movie=obj).aggregate(Avg('rating'))['rating__avg']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
