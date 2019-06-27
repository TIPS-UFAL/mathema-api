from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
from uuid import uuid4


def random_value_generate():
    aleatory_value = uuid4()
    aleatory_value = aleatory_value.hex  # str value
    return aleatory_value[0:8]  # length = 8


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Curriculum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_data = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    group_key = models.CharField(max_length=8, default=random_value_generate, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name='teacher_group', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, through='StudentGroup', blank=True, related_name='student_group')
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class StudentGroup(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    percent_complete = models.FloatField(default=0)

    def __str__(self):
        return "Relação entre: " + self.student.username + " e " + self.group.name


#  Objective não implementado
# class Objective(models.Model):
#     curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=300, null=True, blank=True)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title


class Question(models.Model):
    """
        QUESTION_TYPE_CHOICES:
            1 - Problema: que exige uma resposta escrita
            2 - Múltipla escolha: que exige que a resposta seja uma das propostas
    """
    QUESTION_TYPE_CHOICES = (
        (1, 'problema'),
        (2, 'múltipla escolha'),
    )
    QUESTION_DIFFICULTY_CHOICES = (
        (1, 'iniciante'),
        (2, 'intermediário'),
        (3, 'avançado'),
    )

    difficulty_level = models.PositiveSmallIntegerField(choices=QUESTION_DIFFICULTY_CHOICES, default=1)
    is_private = models.BooleanField(default=False)
    statement = models.TextField()
    title = models.CharField(max_length=100)
    answer = models.TextField()
    type = models.PositiveSmallIntegerField(choices=QUESTION_TYPE_CHOICES, default=1)
    main_tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_principal')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('difficulty_level',)

    def __str__(self):
        return self.title


class TopicCurriculum(models.Model):
    sequence = models.PositiveIntegerField()
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return


class Topic(models.Model):
    # parent_topic = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)  # não implementado
    title = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    curriculum = models.OneToOneField(TopicCurriculum, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, through='QuestionTopic', blank=True, related_name='question_topic')

    def __str__(self):
        return self.title


class QuestionTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "Relação entre: " + self.topic.title + " e " + self.question.title


#  Support não implementado
# class Support(models.Model):
#     title = models.CharField(max_length=100)
#     type = models.CharField(max_length=100)
#     content = models.TextField(default='Dica')
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title


class ModelSolution(models.Model):
    """
        answer: solução modelo com vários passos até se chegar naquela solução
        is_correct: se é um modelo de solução correto ou não
        feedback: alguma explicação sobre o modelo de solução proposto
    """
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=True)
    feedback = models.TextField()

    def __str__(self):
        return 'Modelo de solução da questão: ' + str(self.question)


class ProposedSolution(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return 'Questão: ' + str(self.question) + ' Proprietário: ' + str(self.author)


class Feedback(models.Model):
    EVALUATION_TYPES = (
        (0, 'não avaliado'),
        (1, 'ruim'),
        (2, 'bom'),
        (3, 'excelente'),
    )

    proposed_solution = models.OneToOneField(ProposedSolution, on_delete=models.CASCADE,
                                             primary_key=True)  # chave primária é o prório proposed_solution
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    evaluation = models.PositiveSmallIntegerField(choices=EVALUATION_TYPES, default=0)
    feedback = models.TextField(blank=True, null=True)
    modified_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.modified_date = timezone.now
        self.save()

    def __str__(self):
        return 'Feedback da resposta: ' + str(self.proposed_solution)


class StudentModel(models.Model):
    PERFORMANCE_TYPES = (
        (0, 'não avaliado'),
        (1, 'ruim'),
        (2, 'bom'),
        (3, 'excelente'),
    )

    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    total_sub = models.PositiveIntegerField(default=0)
    total_correct_sub = models.PositiveIntegerField(default=0)
    total_tried_qst = models.PositiveIntegerField(default=0)
    extra_info = models.TextField(blank=True)
    updated_date = models.DateTimeField(default=timezone.now)
    performance = models.PositiveSmallIntegerField(choices=PERFORMANCE_TYPES, default=0)
