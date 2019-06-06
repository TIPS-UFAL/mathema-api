from django.contrib import admin

from .models import Curriculum, Topic, Tag, Question, TopicCurriculum, Topic, QuestionTopic, ModelSolution, \
    User, Group, StudentGroup, ProposedSolution, Feedback, StudentModel

admin.site.register(User)
admin.site.register(Curriculum)
admin.site.register(Topic)
admin.site.register(Group)
admin.site.register(StudentGroup)

