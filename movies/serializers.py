from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):

        if value.year < 1970:
            raise serializers.ValidationError('Data de lançamento não pode ser anterior a 1970')
        else:
            return value

    def validate_resume(self, value):

        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior que 200 caracteres')
        else:
            return value


class MovieStatsSerializer(serializers.Serializer):

    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()


class MovieListDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):

        # Campo caculado: obj é cada um dos objetos de movies
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 2)

        return None


# Este exemplo é um tipo de serializer que não está ligado a model algum
# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset= Genre.objects.all(),
#     )
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset= Actor.objects.all(),
#         many = True,
#     )
#     release_date = serializers.DateField()
#     resume = serializers.CharField()
# reviews = obj.reviews.all() #reviews é o related_name no model de Review campo movie
# if reviews:
#     sum_reviews = 0
#     for review in reviews:
#         sum_reviews += review.stars
#     reviews_count = reviews.count()
#     return round(sum_reviews/reviews_count,2)
# return None
