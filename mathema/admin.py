from django.contrib import admin

from .models import Curriculum, Objective, Suport, Topic, TopicActivity, \
    Activity, TopicSuport, User, Answer, ActivityType

admin.site.register(User)
admin.site.register(Curriculum)
admin.site.register(Objective)
admin.site.register(Suport)
admin.site.register(Topic)
admin.site.register(TopicSuport)
admin.site.register(TopicActivity)
admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(Answer)