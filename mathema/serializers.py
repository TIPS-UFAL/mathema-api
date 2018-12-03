from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Activity, Topic, Group, StudentGroup, \
    Support, Objective, Curriculum, Answer, Evaluation


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


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('evaluation', 'feedback', 'teacher')


class AnswerSerializer(serializers.ModelSerializer):
    evaluation = EvaluationSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        evaluation_data = validated_data.pop('evaluation', None)
        answer = Answer.objects.create(**validated_data)
        # This always creates a Evaluation if the Answer is missing one;
        Evaluation.objects.create(answer=answer, teacher=answer.activity.author, evaluation=None, feedback=None)
        return answer


class UserNamePerPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',)
