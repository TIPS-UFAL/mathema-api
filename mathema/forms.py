from django import forms
from django.forms import ModelForm

from mathema.models import Curriculum, Topico, Objetivo, Atividade

class CurriculumForm(ModelForm):
    class Meta:
        model = Curriculum
        fields = ['titulo', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'descricao', 'ordem', 'topicoPai']

class ObjetivoForm(ModelForm):
    class Meta:
        model = Objetivo
        fields = ['titulo', 'descricao', 'ordem']

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao']
