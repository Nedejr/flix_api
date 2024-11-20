from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        # fields = ['name'] retornar campos específicos
        fields = '__all__'
