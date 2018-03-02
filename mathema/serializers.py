from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Activity, TopicActivity, TopicSupport, Topic, \
    Support, Objective, Curriculum, Answer, ActivityType, TopicCurriculum, Group, StudentGroup


UserModel = get_user_model()


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'is_active', 'user_type',)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'


class TopicCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicCurriculum
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


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class TopicActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicActivity
        fields = '__all__'


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class TopicSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicSupport
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserNamePerPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',)
