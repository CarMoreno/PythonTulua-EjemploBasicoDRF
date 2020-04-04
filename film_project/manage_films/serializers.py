from rest_framework import serializers
from .models import Films

class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'

    def create(self, validated_data):
        new_film = Films(**validated_data)
        new_film.save()
        return new_film

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.fecha_lanzamiento = validated_data.get('fecha_lanzamiento', instance.fecha_lanzamiento)
        instance.genero = validated_data.get('genero', instance.genero)
        instance.puntuacion = validated_data.get('puntuacion', instance.puntuacion)
        instance.sinopsis = validated_data.get('sinopsis', instance.sinopsis)
        instance.fecha_creacion = validated_data.get('fecha_creacion', instance.fecha_creacion)

        instance.save()
        return instance
