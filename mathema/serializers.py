from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Curriculum, Tag, Question, TopicCurriculum, Topic, QuestionTopic, ModelSolution, \
    User, Group, StudentGroup, ProposedSolution, Feedback, StudentModel


UserModel = get_user_model()


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'is_active', 'user_type',)


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TopicCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicCurriculum
        fields = '__all__'


class QuestionTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTopic
        fields = '__all__'


class ModelSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSolution
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class ProposedSolutionSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer(many=False, read_only=True)

    class Meta:
        model = ProposedSolution
        fields = '__all__'

    def create(self, validated_data):
        feedback_data = validated_data.pop('feedback', None)
        proposed_solution = ProposedSolution.objects.create(**validated_data)
        # This always creates a Feedback if the Answer is missing one;
        Feedback.objects.create(proposed_solution=proposed_solution)
        return proposed_solution


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class UserNamePerPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',)
