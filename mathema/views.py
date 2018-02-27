#from django.shortcuts import render #padrao
from django.shortcuts import get_object_or_404
#from django.db.migrations import serializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters

from .models import *
from .serializers import *
from filters.mixins import (FiltersMixin, )
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

"""
    APIREST
"""


"""
    List all Topic, or create a new Topic.
    # api/topic/
    Retrieve, update or delete a Topic instance.
    # api/topic/:id/
"""
class Topic(FiltersMixin, viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-id')
    serializer_class = TopicSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all curriculuns (or a number of curriculuns), or create a new one.
    # api/curriculum
    Retrieve, up  date or delete a curriculum instance.
    # api/curriculum/:pk
    Search curriculuns by title
    # api/curriculum?category='' or api/search?title=
"""
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
    List all TopicActivity, or create a new TopicActivity.
    # api/activityTopic/
    Retrieve, update or delete a TopicActivity instance.
    # api/activityTopic/:id/
"""
class TopicCurriculum(FiltersMixin, viewsets.ModelViewSet):
    queryset = TopicCurriculum.objects.all().order_by('-id')
    serializer_class = TopicCurriculumSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Objective, or create a new Objective.
    # api/objective/
    Retrieve, update or delete a Objective instance.
    # api/objective/:id/
"""
class Objective(FiltersMixin, viewsets.ModelViewSet):
    queryset = Objective.objects.all().order_by('-id')
    serializer_class = ObjectiveSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Activity, or create a new Activity.
    # api/activity/
    Retrieve, update or delete a Activity instance.
    # api/activity/:id/
"""
class ActivityType(FiltersMixin, viewsets.ModelViewSet):
    queryset = ActivityType.objects.all().order_by('-id')
    serializer_class = ActivityTypeSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Activity, or create a new Activity.
    # api/activity/
    Retrieve, update or delete a Activity instance.
    # api/activity/:id/
"""
class Activity(FiltersMixin, viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-id')
    serializer_class = ActivitySerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all TopicActivity, or create a new TopicActivity.
    # api/activityTopic/
    Retrieve, update or delete a TopicActivity instance.
    # api/activityTopic/:id/
"""
class TopicActivity(FiltersMixin, viewsets.ModelViewSet):
    queryset = TopicActivity.objects.all().order_by('-id')
    serializer_class = TopicActivitySerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Supports, or create a new support.
    # api/support/
    Retrieve, update or delete a support instance.
    # api/support/:id/
"""
class Support(FiltersMixin, viewsets.ModelViewSet):
    queryset = Support.objects.all().order_by('-id')
    serializer_class = SupportSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all TopicSuport, or create a new TopicSuport.
    # api/supportTopic/
    Retrieve, update or delete a TopicSuport instance.
    # api/supportTopic/:id/
"""
class TopicSupport(FiltersMixin, viewsets.ModelViewSet):
    queryset = TopicSupport.objects.all().order_by('-id')
    serializer_class = TopicSupportSerializer
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
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Answer.objects.all().order_by('-id')
    serializer_class = AnswerSerializer


"""
    Retrieve a user instance
    # api/user/:pk/
"""
class UserNamePerPK(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def retrieve(selfself, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserNamePerPKSerializer(user)
        return Response(serializer.data)
