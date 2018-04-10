from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
from uuid import uuid4


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,
                                                 default=1)


class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Topic(models.Model):
    parent_topic = models.ForeignKey('self', null=True, blank=True)  # não implementado
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    curriculum = models.ForeignKey(Curriculum)

    def __str__(self):
        return self.title


class Group(models.Model):
    def random_value_generate():
        aleatory_value = uuid4()
        aleatory_value = aleatory_value.hex  # str value
        return aleatory_value[0:8]  # length = 8

    title = models.CharField(max_length=100)
    curriculum = models.ForeignKey(Curriculum)
    group_key = models.CharField(max_length=8, default=random_value_generate, unique=True)
    teacher = models.ForeignKey(User, related_name='teacher_group')
    students = models.ManyToManyField(User, through='StudentGroup', null=True, blank=True, related_name='student_group')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class StudentGroup(models.Model):
    student = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    percent_complete = models.FloatField(default=0)

    def __str__(self):
        return "Relação entre: " + self.student.username + " e " + self.group.title


#  Objective não implementado
class Objective(models.Model):
    curriculum = models.ForeignKey(Curriculum)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        (1, 'problemas'),
        (2, 'multipla escolha'),
    )

    topic = models.ForeignKey(Topic)
    title = models.CharField(max_length=100)
    description = models.TextField()
    models.PositiveSmallIntegerField(choices=ACTIVITY_TYPE_CHOICES,
                                     default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Support(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    content = models.TextField(default='Dica')
    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer = models.TextField()
    activity = models.ForeignKey(Activity)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return 'Question: '+str(self.activity)+' Proprietario: '+str(self.author)


class Evaluation(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, primary_key=True)  # chave primária é a prória answer
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL)
    evaluation = models.IntegerField(null=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Answer: '+str(self.answer)+' Proprietario: '+str(self.answer.author)+'Avaliação: '+str(self.evaluation)





