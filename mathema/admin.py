from django.contrib import admin

from .models import Curriculum, Objective, Support, Topic, \
    Activity, User, Answer, Evaluation, Group, StudentGroup

admin.site.register(User)
admin.site.register(Curriculum)
admin.site.register(Topic)
admin.site.register(Group)
admin.site.register(StudentGroup)
admin.site.register(Objective)
admin.site.register(Activity)
admin.site.register(Support)
admin.site.register(Answer)
admin.site.register(Evaluation)
