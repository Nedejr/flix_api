# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# import json
from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


# Lista e cria substitui a função genre_create_list_view
class GenreCreateListView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()  # retorna todos os objetos
    # queryset = Genre.objects.filter(name='Terror') # retorna apenas gênero Terror
    serializer_class = GenreSerializer


# Busca, atualiza e Deleta
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


"""

@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        #genres => 'django.db.models.query.QuerySet'
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        #data => dict
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name},
                             status=201)

@csrf_exempt
def genre_detail_view(request,pk):

    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name}, status=203)

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Genêro excluido com sucesso'}, status=204)
"""
