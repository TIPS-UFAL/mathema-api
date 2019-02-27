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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Topic(models.Model):
    parent_topic = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)  # não implementado
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Group(models.Model):
    def random_value_generate():
        aleatory_value = uuid4()
        aleatory_value = aleatory_value.hex  # str value
        return aleatory_value[0:8]  # length = 8

    group_key = models.CharField(max_length=8, default=random_value_generate, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name='teacher_group', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, through='StudentGroup', blank=True, related_name='student_group')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class StudentGroup(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    percent_complete = models.FloatField(default=0)

    def __str__(self):
        return "Relação entre: " + self.student.username + " e " + self.group.title


#  Objective não implementado
class Objective(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = (
        (1, 'problemas'),
        (2, 'multipla escolha'),
    )
    ACTIVITY_DIFFICULTY_CHOICES = (
        (1, 'iniciante'),
        (2, 'intermediario'),
        (3, 'avançado'),
    )

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.TextField()
    difficulty = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Support(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    content = models.TextField(default='Dica')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return 'Question: '+str(self.activity)+' Proprietario: '+str(self.author)


class Evaluation(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, primary_key=True)  # chave primária é a prória answer
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evaluation = models.IntegerField(null=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Answer: '+str(self.answer)+' Proprietario: '+str(self.answer.author)+'Avaliação: '+str(self.evaluation)





