#from django.shortcuts import render #padrao
#from django.shortcuts import get_object_or_404
#from django.db.migrations import serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from .models import *
from .serializers import *
from filters.mixins import (FiltersMixin, )
# from rest_framework import permissions


"""
    APIREST
"""


# List all curriculuns (or a number of curriculuns), or create a new one.
# api/curriculum
# Retrieve, up  date or delete a curriculum instance.
# api/curriculum/:pk
# Search curriculuns by title
# api/curriculum?category='' or api/search?title=
class Curriculum(FiltersMixin, viewsets.ModelViewSet):
    # permission_classes = permissions.IsAuthenticatedOrReadOnly
    queryset = Curriculum.objects.all().order_by('-id')
    serializer_class = CurriculumSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo',)
    filter_mappings = {
        'title': 'titulo',
    }


"""
    List all Supports, or create a new support.
    # api/support/
    Retrieve, update or delete a support instance.
    # api/support/:id/
"""
class Suporte(FiltersMixin, viewsets.ModelViewSet):
    queryset = Suporte.objects.all().order_by('-id')
    serializer_class = SuporteSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Atividade, or create a new Atividade.
    # api/activity/
    Retrieve, update or delete a Atividade instance.
    # api/activity/:id/
"""
class Atividade(FiltersMixin, viewsets.ModelViewSet):
    queryset = Atividade.objects.all().order_by('-id')
    serializer_class = AtividadeSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Answers, or create a new Answer.
    # api/answer/
    Retrieve, update or delete a Answer instance.
    # api/answer/:id/
"""
class Answer(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-id')
    serializer_class = AnswerSerializer


"""
    List all Topico, or create a new Topico.
    # api/topic/
    Retrieve, update or delete a Topico instance.
    # api/topic/:id/
"""
class Topico(FiltersMixin, viewsets.ModelViewSet):
    queryset = Topico.objects.all().order_by('-id')
    serializer_class = TopicoSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Objetivo, or create a new Objetivo.
    # api/objective/
    Retrieve, update or delete a Objetivo instance.
    # api/objective/:id/
"""
class Objetivo(FiltersMixin, viewsets.ModelViewSet):
    queryset = Objetivo.objects.all().order_by('-id')
    serializer_class = ObjetivoSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all TipoSuporte, or create a new TipoSuporte.
    # api/supportType/
    Retrieve, update or delete a TipoSuporte instance.
    # api/supportType/:id/
"""
class TipoSuporte(FiltersMixin, viewsets.ModelViewSet):
    queryset = TipoSuporte.objects.all().order_by('-id')
    serializer_class = TipoSuporteSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all TopicoAtividade, or create a new TopicoAtividade.
    # api/activityTopic/
    Retrieve, update or delete a TopicoAtividade instance.
    # api/activityTopic/:id/
"""
class TopicoAtividade(FiltersMixin, viewsets.ModelViewSet):
    queryset = TopicoAtividade.objects.all().order_by('-id')
    serializer_class = TopicoAtividadeSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all TopicoSuporte, or create a new TopicoSuporte.
    # api/supportTopic/
    Retrieve, update or delete a TopicoSuporte instance.
    # api/supportTopic/:id/
"""
class TopicoSuporte(FiltersMixin, viewsets.ModelViewSet):
    queryset = TopicoSuporte.objects.all().order_by('-id')
    serializer_class = TopicoSuporteSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }
