#from django.shortcuts import render #padrao
from django.shortcuts import get_object_or_404
#from django.db.migrations import serializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, viewsets, filters, generics, mixins

from .models import *
from .models import Answer as AnswerModel, Activity as ActivityModel, Support as SupportModel, Topic as TopicModel
from .serializers import *
from filters.mixins import (FiltersMixin, )
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacher, IsOwnerOrReadOnly

"""
    APIREST
"""


"""
    List all curriculuns (or a number of curriculuns), or create a new one.
    # api/curriculum
    Retrieve, up  date or delete a curriculum instance.
    # api/curriculum/:pk
    Search curriculuns by title
    # api/curriculum?category='' or api/search?title=
"""
class Curriculum(FiltersMixin, viewsets.ModelViewSet):
    queryset = Curriculum.objects.all().order_by('-id')
    serializer_class = CurriculumSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('titulo',)
    filter_mappings = {
        'title': 'titulo',
    }


"""
    List all Topic, or create a new Topic.
    # api/topic/
    Retrieve, update or delete a Topic instance.
    # api/topic/:id/
"""
class Topic(FiltersMixin, viewsets.GenericViewSet,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin):

    queryset = TopicModel.objects.all()
    serializer_class = TopicSerializer

    def list(self, request, pk_curriculum):
        queryset = TopicModel.objects.filter(curriculum=pk_curriculum)
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)

#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all Group, or create a new Group.
    # api/group/
    Retrieve, update or delete a Group instance.
    # api/group/:id/
"""
class Group(FiltersMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('titulo',)
#     filter_mappings = {
#         'title': 'titulo',
#     }


"""
    List all StudentGroup, or create a new StudentGroup.
    # api/studentGroup/
    Retrieve, update or delete a StudentGroup instance.
    # api/studentGroup/:id/
"""
class StudentGroup( viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all().order_by('-id')
    serializer_class = StudentGroupSerializer


"""
    List all Objective, or create a new Objective.
    # api/objective/
    Retrieve, update or delete a Objective instance.
    # api/objective/:id/
"""
class Objective(FiltersMixin, viewsets.ModelViewSet):
    queryset = Objective.objects.all().order_by('-id')
    serializer_class = ObjectiveSerializer


"""
    List all Activity, or create a new Activity.
    # api/activity/
    Retrieve, update or delete a Activity instance.
    # api/activity/:id/
"""
class Activity(viewsets.GenericViewSet,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin):

    queryset = ActivityModel.objects.all()
    serializer_class = ActivitySerializer

    def list(self, request, pk_topic):
        queryset = ActivityModel.objects.filter(topic=pk_topic)
        serializer = ActivitySerializer(queryset, many=True)
        return Response(serializer.data)


"""
    List all Supports, or create a new support.
    # api/support/
    Retrieve, update or delete a support instance.
    # api/support/:id/
"""
class Support(viewsets.GenericViewSet,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin):

    queryset = SupportModel.objects.all()
    serializer_class = SupportSerializer

    def list(self, request, pk_topic):
        queryset = SupportModel.objects.filter(topic=pk_topic)
        serializer = SupportSerializer(queryset, many=True)
        return Response(serializer.data)


"""
    List all Answers, or create a new Answer.
    # api/answer/
    Retrieve, update or delete a Answer instance.
    # api/answer/:id/
"""
class Answer(viewsets.GenericViewSet,
             mixins.CreateModelMixin,
             mixins.DestroyModelMixin,
             mixins.UpdateModelMixin,
             mixins.RetrieveModelMixin):

    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        print(self)
        print(self.action)
        if self.action == 'list':
            permission_classes = [IsTeacher, IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

        return [permission() for permission in permission_classes]

    def list(self, request, pk_activity):
        queryset = AnswerModel.objects.filter(activity=pk_activity).order_by('-id')
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)


"""
    Retrieve a user instance
    # api/user/:pk/
"""
class UserNamePerPK(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserNamePerPKSerializer(user)
        return Response(serializer.data)
