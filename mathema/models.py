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
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    data_criacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.titulo


class Objetivo(models.Model):
    curriculum = models.ForeignKey(Curriculum)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.titulo


class TipoSuporte(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Suporte(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoSuporte)
    arquivo = models.FileField(upload_to='suporte', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.titulo


class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer = models.TextField()
    activity = models.ForeignKey(Atividade)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return 'Questão: '+str(self.activity)+' Proprietario: '+str(self.owner)


class Topico(models.Model):
    objetivo = models.ForeignKey(Objetivo)
    topicoPai = models.ForeignKey('self', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    suportes = models.ManyToManyField(Suporte, through='TopicoSuporte', null=True, blank=True)
    atividades = models.ManyToManyField(Atividade, through='TopicoAtividade', null=True, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.titulo


class TopicoAtividade(models.Model):
    topico = models.ForeignKey(Topico)
    atividade = models.ForeignKey(Atividade)

    def __str__(self):
        return self.topico.titulo + " possui " + self.atividade.titulo


class TopicoSuporte(models.Model):
    topico = models.ForeignKey(Topico)
    suporte = models.ForeignKey(Suporte)

    def __str__(self):
        return self.topico.titulo + " possui " + self.suporte.titulo + " (" + self.suporte.tipo + ") "




