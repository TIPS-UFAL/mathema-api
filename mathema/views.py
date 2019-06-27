from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets, filters, generics, mixins
from django.contrib.auth.models import User

from .models import Topic as TopicModel, TopicCurriculum as TCModel, \
    StudentGroup as StudentGroupModel, Group as GroupModel, Question as QuestionModel, ModelSolution as MSModel, \
    ProposedSolution as PSModel, Feedback as FeedbackModel, StudentModel as SMModel
from .serializers import *
from filters.mixins import (FiltersMixin, )
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTeacher, IsOwnerOrReadOnly, IsOwner, IsOwnerOrTeacher

"""
    APIREST
"""


class Tag(FiltersMixin, viewsets.GenericViewSet,
          mixins.ListModelMixin,
          mixins.RetrieveModelMixin):
    """
        List all curriculums (or a number of curriculuns), or create a new one.
        # api/curriculum
        Retrieve, up  date or delete a curriculum instance.
        # api/curriculum/:pk
        Search curriculuns by title
        # api/curriculum?title='' or api/curriculum?search=''
    """
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    filter_mappings = {
        'name': 'name',
    }


class Curriculum(FiltersMixin, viewsets.ModelViewSet):
    """
        List all curriculums (or a number of curriculuns), or create a new one.
        # api/curriculum
        Retrieve, up  date or delete a curriculum instance.
        # api/curriculum/:pk
        Search curriculuns by title
        # api/curriculum?title='' or api/curriculum?search=''
    """
    permission_classes = (IsAuthenticated, IsTeacher,)

    queryset = Curriculum.objects.all().order_by('-id')
    serializer_class = CurriculumSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    filter_mappings = {
        'title': 'title',
        'author': 'author'
    }


class Group(viewsets.GenericViewSet,
            mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin):
    """
        List all Group, or create a new Group.
        # api/group/
        Retrieve, update or delete a Group instance.
        # api/group/:id/
        Search groups by group_key
        # api/group?group_key='' or api/group?search=''
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer

    def list(self, request):
        queryset = GroupModel.objects.filter(visible=True)
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('group_key',)
    filter_mappings = {
        'name': 'name',
        'group_key': 'group_key',
        'teacher': 'teacher'
    }


class StudentGroup(FiltersMixin,
                   viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    """
        List all StudentGroup, or create a new StudentGroup.
        # api/studentGroup/
        Retrieve, update or delete a StudentGroup instance.
        # api/studentGroup/:id_student/:id_group
    """
    queryset = StudentGroupModel.objects.all().order_by('-id')
    serializer_class = StudentGroupSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsTeacher, IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk_student=None, pk_group=None):
        queryset = StudentGroupModel.objects.filter(student=pk_student, group=pk_group)
        group = get_object_or_404(self.queryset, pk=queryset)
        serializer = StudentGroupSerializer(group)
        return Response(serializer.data)


class Question(FiltersMixin, viewsets.ModelViewSet):
    """
        List all Activity, or create a new Activity.
        # api/activity/
        Retrieve, update or delete a Activity instance.
        # api/activity/:id/
    """
    # Todo: filtrar se é privado ou não no caso de retrieve e list, testar se colocando aqui, o create, o destroy e o
    #  update ficam normal
    queryset = QuestionModel.objects.all().order_by('difficulty_level')
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsTeacher, IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

        return [permission() for permission in permission_classes]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'main_tag', 'tags')
    filter_mappings = {
        'title': 'title',
        'difficulty_level': 'difficulty_level',
        'main_tag': 'main_tag',
        'tags': 'tags'
    }


class TopicCurriculum(FiltersMixin, viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin):
    # Todo: se Topic já vier ordenado na sequência correta, não precisa dessa View
    """
        List all Topic, or create a new Topic.
        # api/topic/
        Retrieve, update or delete a Topic instance.
        # api/topic/:id/
    """
    queryset = TCModel.objects.all()
    serializer_class = TopicSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsTeacher, IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

        return [permission() for permission in permission_classes]


class Topic(viewsets.GenericViewSet,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin,
            mixins.UpdateModelMixin,
            mixins.RetrieveModelMixin):
    """
        List all Topic, or create a new Topic.
        # api/topic/
        Retrieve, update or delete a Topic instance.
        # api/topic/:id/
    """
    queryset = TopicModel.objects.all()
    serializer_class = TopicSerializer

    def list(self, request, pk_curriculum):
        queryset = TopicModel.objects.filter(curriculum=pk_curriculum).order_by('curriculum.sequence')
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsTeacher, IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

        return [permission() for permission in permission_classes]


class ModelSolution(FiltersMixin, viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin):
    """
        List all StudentGroup, or create a new StudentGroup.
        # api/studentGroup/
        Retrieve, update or delete a StudentGroup instance.
        # api/studentGroup/:id_student/:id_group
    """
    queryset = MSModel.objects.all()
    serializer_class = ModelSolutionSerializer

    def list(self, request, pk_question):
        queryset = MSModel.objects.filter(question=pk_question)
        serializer = ModelSolutionSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsTeacher, IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        return [permission() for permission in permission_classes]


class ProposedSolution(FiltersMixin, viewsets.GenericViewSet,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin):
    """
        List all StudentGroup, or create a new StudentGroup.
        # api/studentGroup/
        Retrieve, update or delete a StudentGroup instance.
        # api/studentGroup/:id_student/:id_group
    """
    queryset = PSModel.objects.all()
    serializer_class = ProposedSolutionSerializer

    def list(self, request, pk_group, pk_question):
        group = GroupModel.objects.get(id=pk_group)
        queryset = PSModel.objects.filter(question=pk_question, author__in=group.students)
        serializer = ProposedSolutionSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsOwner, IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsOwnerOrTeacher, IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsTeacher, IsAuthenticated]

        return [permission() for permission in permission_classes]


class Feedback(FiltersMixin, viewsets.GenericViewSet,
               mixins.UpdateModelMixin):
    """
        List all StudentGroup, or create a new StudentGroup.
        # api/studentGroup/
        Retrieve, update or delete a StudentGroup instance.
        # api/studentGroup/:id_student/:id_group
    """
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer

    def retrieve(self, request, pk_psolution):
        feedback = get_object_or_404(self.queryset, proposed_solution=pk_psolution)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'update':
            permission_classes = [IsTeacher, IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsOwnerOrTeacher, IsAuthenticated]

        return [permission() for permission in permission_classes]


class UserNamePerPK(viewsets.ViewSet):
    """
        Retrieve a user instance
        # api/user/:pk/
    """
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserNamePerPKSerializer(user)
        return Response(serializer.data)
