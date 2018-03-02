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


class Topic(models.Model):
    parent_topic = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    topics = models.ManyToManyField(Topic, through='TopicCurriculum', null=True, blank=True)

    def __str__(self):
        return self.title


class TopicCurriculum(models.Model):
    topic = models.ForeignKey(Topic)
    curriculum = models.ForeignKey(Curriculum)

    def __str__(self):
        return "Relação entre: " + self.topic.title + " e " + self.curriculum.title


class Group(models.Model):
    title = models.CharField(max_length=100)
    curriculum = models.ForeignKey(Curriculum)
    group_key = models.CharField(max_length=10)
    teacher = models.ForeignKey(User, related_name='teacher_group')
    students = models.ManyToManyField(User, through='StudentGroup', null=True, blank=True, related_name='student_group')

    def __str__(self):
        return self.title


class StudentGroup(models.Model):
    student = models.ForeignKey(User)
    group = models.ForeignKey(Group )

    def __str__(self):
        return "Relação entre: " + self.student.id + " e " + self.group.title


class Objective(models.Model):
    curriculum = models.ForeignKey(Curriculum)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class ActivityType(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        (1, 'problemas'),
        (2, 'multipla escolha'),
    )

    activity_type = models.PositiveSmallIntegerField(choices=ACTIVITY_TYPE_CHOICES,
                                                     default=1)

    def __str__(self):
        return self.activity_type


class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.ForeignKey(ActivityType, null=True)
    topics = models.ManyToManyField(Topic, through='TopicActivity', null=True, blank=True)

    def __str__(self):
        return self.title


class TopicActivity(models.Model):
    topic = models.ForeignKey(Topic)
    activity = models.ForeignKey(Activity, default=0)

    def __str__(self):
        return "Relação entre: " + self.topic.title + " e " + self.activity.title


class Support(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    content = models.TextField(default='Dica')
    topics = models.ManyToManyField(Topic, through='TopicSupport', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class TopicSupport(models.Model):
    topic = models.ForeignKey(Topic)
    support = models.ForeignKey(Support)

    def __str__(self):
        return "Relação entre: " + self.topic.title + " e " + self.support.title + " (" + self.support.type + ") "


class Answer(models.Model):
    answer = models.TextField()
    activity = models.ForeignKey(Activity)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    evaluation = models.IntegerField(default=0)

    def __str__(self):
        return 'Question: '+str(self.activity)+' Proprietario: '+str(self.author)







