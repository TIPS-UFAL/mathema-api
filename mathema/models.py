from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,
                                                 default=1)


class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    creation_data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Objective(models.Model):
    curriculum = models.ForeignKey(Curriculum)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class ActivityType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Topic(models.Model):
    parent_topic = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(ActivityType, null=True)
    topics = models.ManyToManyField(Topic, through='TopicActivity', null=True, blank=True)

    def __str__(self):
        return self.title


class Suport(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    content = models.TextField(default='Dica')
    topics = models.ManyToManyField(Topic, through='TopicSuport', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer = models.TextField()
    activity = models.ForeignKey(Activity)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    evaluation = models.IntegerField(default=0)

    def __str__(self):
        return 'Question: '+str(self.activity)+' Proprietario: '+str(self.owner)

    
class TopicActivity(models.Model):
    topic = models.ForeignKey(Topic)
    activity = models.ForeignKey(Activity, null=True)

    def __str__(self):
        return self.topic.title + " possui " + self.activity.title


class TopicSuport(models.Model):
    topic = models.ForeignKey(Topic)
    support = models.ForeignKey(Suport)

    def __str__(self):
        return self.topic.title + " possui " + self.support.title + " (" + self.support.type + ") "




