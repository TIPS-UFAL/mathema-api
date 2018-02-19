from django.contrib import admin

from .models import Curriculum, Objective, Support, Topic, TopicActivity, \
    Activity, TopicSupport, User, Answer, ActivityType

admin.site.register(User)
admin.site.register(Curriculum)
admin.site.register(Objective)
admin.site.register(Support)
admin.site.register(Topic)
admin.site.register(TopicSupport)
admin.site.register(TopicActivity)
admin.site.register(Activity)
admin.site.register(ActivityType)
admin.site.register(Answer)