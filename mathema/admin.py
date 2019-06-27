from django.contrib import admin

from .models import Curriculum, Tag, Question, TopicCurriculum, Topic, QuestionTopic, ModelSolution, \
    User, Group, StudentGroup, ProposedSolution, Feedback, StudentModel

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Curriculum)
admin.site.register(Group)
admin.site.register(StudentGroup)
admin.site.register(Question)
admin.site.register(TopicCurriculum)
admin.site.register(Topic)
admin.site.register(QuestionTopic)
admin.site.register(ModelSolution)
admin.site.register(ProposedSolution)
admin.site.register(Feedback)
admin.site.register(StudentModel)

