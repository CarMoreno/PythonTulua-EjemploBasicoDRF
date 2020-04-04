from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Films
from .serializers import FilmsSerializer

class ListFilms(APIView):
    def get(self, request):
        films = Films.objects.all()
        data_serializer = FilmsSerializer(films, many=True)
        return Response(data_serializer.data, HTTP_200_OK)

class CreateFilms(APIView):
    def post(self, request):
        new_film = FilmsSerializer(data=request.data)
        if new_film.is_valid():
            new_film.save()
            return Response(new_film.validated_data, HTTP_201_CREATED)
        return Response(HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateFilms(APIView):
    def put(self, request, pk):
        film_in_db = get_object_or_404(Films, pk=pk)
        film_serializer = FilmsSerializer(instance=film_in_db, data=request.data, partial=True)
        if film_serializer.is_valid():
            film_saved = film_serializer.save()
            # Ejemplo donde retornamos una respuesta personalizada
            return Response({ "status": "success", "message": "Film {} update correctly".format(film_saved.nombre)}, HTTP_200_OK)
        return Response(HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteFilms(APIView):
    def delete(self, request, pk):
        film = get_object_or_404(Films, pk=pk)
        film.delete()
        return Response(HTTP_204_NO_CONTENT)

class DetailFilms(APIView):
    def get(self, request, pk):
        film = get_object_or_404(Films, pk=pk)
        data = FilmsSerializer(film).data
        return Response(data, HTTP_200_OK)