from django import forms
from django.forms import ModelForm

from mathema.models import Curriculum, Topic, Objective, Activity

class CurriculumForm(ModelForm):
    class Meta:
        model = Curriculum
        fields = ['titulo', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['titulo', 'descricao', 'ordem', 'topicPai']

class ObjectiveForm(ModelForm):
    class Meta:
        model = Objective
        fields = ['titulo', 'descricao', 'ordem']

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['titulo', 'descricao']
