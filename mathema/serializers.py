from django.conf import settings
from rest_framework import serializers
from .models import Activity, TopicActivity, TopicSupport, Topic, \
    Support, Objective, Curriculum, Answer, ActivityType


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicActivity
        fields = '__all__'


class TopicSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicSupport
        fields = '__all__'



class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'is_active', 'user_type',)