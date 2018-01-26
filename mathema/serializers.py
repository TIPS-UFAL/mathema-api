from django.conf import settings
from rest_framework import serializers
from .models import Atividade, TopicoAtividade, TopicoSuporte, Topico, TipoSuporte, \
    Suporte, Objetivo, Curriculum, Answer


class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class TopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico
        fields = '__all__'


class TopicoAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicoAtividade
        fields = '__all__'


class TopicoSuporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicoSuporte
        fields = '__all__'


class TipoSuporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSuporte
        fields = '__all__'


class SuporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suporte
        fields = '__all__'


class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = '__all__'


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'is_active', 'user_type',)