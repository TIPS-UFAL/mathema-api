from django.contrib import admin

from .models import Curriculum, Topic, \
    User, Group, StudentGroup

admin.site.register(User)
admin.site.register(Curriculum)
admin.site.register(Topic)
admin.site.register(Group)
admin.site.register(StudentGroup)

